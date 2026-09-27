/*
 * IRL™ native core accelerator — the first non-.py engine component.
 * Copyright (C) 2026 Anika Mukherjee. AGPL-3.0-or-later.
 *
 * _irl_native.lex_fast(source) -> list of (kind, value, line, col) tuples,
 * matching the reference Python lexer's token stream (canonical keywords,
 * legacy aliases, # and // comments, string escapes, raw f-string capture,
 * NEWLINE + EOF sentinels).
 *
 * Compiled to machine code per platform; ships as a prebuilt wheel via CI.
 * If this module is absent the pure-Python lexer is used — same output.
 *
 * Design notes: kind names live in a table of interned PyObjects created
 * once at module init (Py_INCREF'd into each tuple — no per-token kind
 * allocations, no leaks). String values are built in a single buffer with
 * escape processing done in plain C, then converted once — no refcount
 * churn in the hot loop.
 */

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>
#include <string.h>

enum Kind {
    K_NUMBER, K_STRING, K_FSTRING, K_KEYWORD, K_IDENT,
    K_NEWLINE, K_EOF,
    K_EQEQ, K_NEQ, K_LTE, K_GTE, K_ASSIGN, K_LT, K_GT,
    K_PLUS, K_MINUS, K_MUL, K_DIV, K_SEMI, K_COMMA, K_COLON, K_DOT,
    K_LPAREN, K_RPAREN, K_LBRACE, K_RBRACE, K_LBRACKET, K_RBRACKET,
    K_POWER,
    NKINDS
};

static PyObject *KIND[NKINDS];

static const char *KIND_NAMES[NKINDS] = {
    "NUMBER", "STRING", "FSTRING", "KEYWORD", "IDENT",
    "NEWLINE", "EOF",
    "EQEQ", "NEQ", "LTE", "GTE", "ASSIGN", "LT", "GT",
    "PLUS", "MINUS", "MUL", "DIV", "SEMI", "COMMA", "COLON", "DOT",
    "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET",
    "POWER",
};

/* spelling -> canonical; iskw=1 -> KEYWORD kind, 0 -> IDENT kind */
typedef struct { const char *spell; const char *canon; int iskw; } WordEntry;

static const WordEntry WORDS[] = {
    {"var", "var", 1}, {"let", "var", 1}, {"snag", "var", 1},
    {"function", "function", 1}, {"def", "function", 1},
    {"fn", "function", 1}, {"task", "function", 1},
    {"if", "if", 1}, {"bet", "if", 1},
    {"elif", "elif", 1},
    {"else", "else", 1}, {"cap", "else", 1},
    {"while", "while", 1}, {"grind", "while", 1},
    {"for", "for", 1}, {"in", "in", 1},
    {"break", "break", 1}, {"continue", "continue", 1},
    {"return", "return", 1}, {"brb", "return", 1},
    {"true", "true", 1}, {"fax", "true", 1},
    {"false", "false", 1}, {"fake", "false", 1},
    {"none", "none", 1},
    {"memo", "memo", 1}, {"import", "import", 1},
    {"and", "and", 1}, {"fr", "and", 1},
    {"or", "or", 1},
    {"not", "not", 1}, {"nah", "not", 1},
    {"spill", "print", 0}, {"ask", "input", 0}, {"push", "append", 0},
};
#define NWORDS (sizeof(WORDS) / sizeof(WORDS[0]))

static int
word_lookup(const char *s, Py_ssize_t len, const char **canon, int *iskw)
{
    for (size_t i = 0; i < NWORDS; i++) {
        if ((Py_ssize_t)strlen(WORDS[i].spell) == len
            && memcmp(WORDS[i].spell, s, len) == 0) {
            *canon = WORDS[i].canon;
            *iskw = WORDS[i].iskw;
            return 1;
        }
    }
    return 0;
}

/* returns the mapped escape char, 0 = keep backslash + next char */
static char
escape_char(char c)
{
    switch (c) {
    case 'n': return '\n';
    case 't': return '\t';
    case 'r': return '\r';
    case '"': return '"';
    case '\\': return '\\';
    case '{': return '{';
    case '}': return '}';
    default: return 0;
    }
}

static PyObject *
make_token(int kind, PyObject *value /* stolen */, long line, long col)
{
    PyObject *tok = Py_BuildValue("(OOll)", KIND[kind], value, line, col);
    Py_DECREF(value);
    return tok;
}

static PyObject *
make_token_text(int kind, const char *start, Py_ssize_t len,
                long line, long col)
{
    PyObject *value = PyUnicode_FromStringAndSize(start, len);
    if (value == NULL) {
        return NULL;
    }
    return make_token(kind, value, line, col);
}

static int
append_token(PyObject *out, PyObject *tok)
{
    if (tok == NULL || PyList_Append(out, tok) < 0) {
        Py_XDECREF(tok);
        return -1;
    }
    Py_DECREF(tok);
    return 0;
}

/* Scan a double-quoted string starting at src[i] == '"'.
 * On success: *out_value = decoded contents (new ref), *end = index after
 * closing quote. Returns 0 on success, -1 on Python error, -2 = unterminated. */
static int
scan_string(const char *src, Py_ssize_t srclen, Py_ssize_t i,
            PyObject **out_value, Py_ssize_t *end)
{
    Py_ssize_t j = i + 1;
    size_t cap = 32, len = 0;
    char *buf = malloc(cap);
    if (buf == NULL) {
        PyErr_NoMemory();
        return -1;
    }
    while (j < srclen && src[j] != '"') {
        char ch = src[j];
        char decoded[2];
        const char *piece = &ch;
        size_t plen = 1;
        if (ch == '\\' && j + 1 < srclen) {
            char mapped = escape_char(src[j + 1]);
            if (mapped == 0) {
                decoded[0] = '\\';
                decoded[1] = src[j + 1];
                piece = decoded;
                plen = 2;
            } else {
                decoded[0] = mapped;
                piece = decoded;
                plen = 1;
            }
            j += 2;
        } else {
            j++;
        }
        if (len + plen + 1 > cap) {
            cap *= 2;
            char *nb = realloc(buf, cap);
            if (nb == NULL) {
                free(buf);
                PyErr_NoMemory();
                return -1;
            }
            buf = nb;
        }
        memcpy(buf + len, piece, plen);
        len += plen;
    }
    if (j >= srclen) {
        free(buf);
        return -2;
    }
    PyObject *value = PyUnicode_DecodeUTF8(buf, (Py_ssize_t)len, "strict");
    free(buf);
    if (value == NULL) {
        return -1;
    }
    *out_value = value;
    *end = j + 1;
    return 0;
}

static PyObject *
irl_lex_fast(PyObject *self, PyObject *args)
{
    const char *src;
    Py_ssize_t srclen;
    if (!PyArg_ParseTuple(args, "s#", &src, &srclen)) {
        return NULL;
    }

    PyObject *out = PyList_New(0);
    if (out == NULL) {
        return NULL;
    }

    Py_ssize_t i = 0;
    long line = 1;
    Py_ssize_t line_start = 0;

    while (i < srclen) {
        char c = src[i];
        long col = (long)(i - line_start) + 1;

        if (c == '\n') {
            if (append_token(out, make_token(K_NEWLINE,
                    PyUnicode_FromString("\\n"), line, col)) < 0) {
                Py_DECREF(out);
                return NULL;
            }
            i++;
            line++;
            line_start = i;
            continue;
        }
        if (c == ' ' || c == '\t' || c == '\r') {
            i++;
            continue;
        }
        if (c == '#') {
            while (i < srclen && src[i] != '\n') {
                i++;
            }
            continue;
        }
        if (c == '/' && i + 1 < srclen && src[i + 1] == '/') {
            while (i < srclen && src[i] != '\n') {
                i++;
            }
            continue;
        }
        if (c == '"' || (c == 'f' && i + 1 < srclen && src[i + 1] == '"')) {
            int is_fstring = (c == 'f');
            Py_ssize_t open = is_fstring ? i + 1 : i;
            PyObject *value = NULL;
            Py_ssize_t end = 0;
            int rc = scan_string(src, srclen, open, &value, &end);
            if (rc == -2) {
                PyErr_Format(PyExc_ValueError, "\x01%ld\x01%ld\x01Unterminated string.",
                             line, col);
                Py_DECREF(out);
                return NULL;
            }
            if (rc != 0) {
                Py_DECREF(out);
                return NULL;
            }
            /* f-strings keep raw inner text (escapes handled by parser) */
            PyObject *tok;
            if (is_fstring) {
                Py_ssize_t rawlen = (end - 1) - (open + 1);
                Py_DECREF(value);
                tok = make_token_text(K_FSTRING, src + open + 1, rawlen, line, col);
            } else {
                tok = make_token(K_STRING, value, line, col);
            }
            if (append_token(out, tok) < 0) {
                Py_DECREF(out);
                return NULL;
            }
            i = end;
            continue;
        }
        if (c >= '0' && c <= '9') {
            Py_ssize_t j = i;
            while (j < srclen && src[j] >= '0' && src[j] <= '9') {
                j++;
            }
            if (j < srclen && src[j] == '.' && j + 1 < srclen
                && src[j + 1] >= '0' && src[j + 1] <= '9') {
                j++;
                while (j < srclen && src[j] >= '0' && src[j] <= '9') {
                    j++;
                }
            }
            PyObject *tok = make_token_text(K_NUMBER, src + i, j - i, line, col);
            if (append_token(out, tok) < 0) {
                Py_DECREF(out);
                return NULL;
            }
            i = j;
            continue;
        }
        if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || c == '_') {
            Py_ssize_t j = i;
            while (j < srclen
                   && ((src[j] >= 'a' && src[j] <= 'z')
                       || (src[j] >= 'A' && src[j] <= 'Z')
                       || (src[j] >= '0' && src[j] <= '9') || src[j] == '_')) {
                j++;
            }
            const char *canon;
            int iskw;
            PyObject *tok;
            if (word_lookup(src + i, j - i, &canon, &iskw)) {
                PyObject *val = PyUnicode_FromString(canon);
                if (val == NULL) {
                    Py_DECREF(out);
                    return NULL;
                }
                tok = make_token(iskw ? K_KEYWORD : K_IDENT, val, line, col);
            } else {
                tok = make_token_text(K_IDENT, src + i, j - i, line, col);
            }
            if (append_token(out, tok) < 0) {
                Py_DECREF(out);
                return NULL;
            }
            i = j;
            continue;
        }

        /* two-char operators */
        if (i + 1 < srclen) {
            char c1 = src[i], c2 = src[i + 1];
            int kind = -1;
            if (c1 == '*' && c2 == '*') kind = K_POWER;
            else if (c1 == '=' && c2 == '=') kind = K_EQEQ;
            else if (c1 == '!' && c2 == '=') kind = K_NEQ;
            else if (c1 == '<' && c2 == '=') kind = K_LTE;
            else if (c1 == '>' && c2 == '=') kind = K_GTE;
            if (kind >= 0) {
                PyObject *tok = make_token_text(kind, src + i, 2, line, col);
                if (append_token(out, tok) < 0) {
                    Py_DECREF(out);
                    return NULL;
                }
                i += 2;
                continue;
            }
        }

        /* single-char tokens */
        int kind = -1;
        switch (c) {
        case '=': kind = K_ASSIGN; break;
        case '<': kind = K_LT; break;
        case '>': kind = K_GT; break;
        case '+': kind = K_PLUS; break;
        case '-': kind = K_MINUS; break;
        case '*': kind = K_MUL; break;
        case '/': kind = K_DIV; break;
        case ';': kind = K_SEMI; break;
        case ',': kind = K_COMMA; break;
        case ':': kind = K_COLON; break;
        case '.': kind = K_DOT; break;
        case '(': kind = K_LPAREN; break;
        case ')': kind = K_RPAREN; break;
        case '{': kind = K_LBRACE; break;
        case '}': kind = K_RBRACE; break;
        case '[': kind = K_LBRACKET; break;
        case ']': kind = K_RBRACKET; break;
        default: kind = -1; break;
        }
        if (kind >= 0) {
            PyObject *tok = make_token_text(kind, src + i, 1, line, col);
            if (append_token(out, tok) < 0) {
                Py_DECREF(out);
                return NULL;
            }
            i++;
            continue;
        }

        Py_DECREF(out);
        PyErr_Format(PyExc_ValueError, "\x01%ld\x01%ld\x01Unexpected character '%c'.",
                     line, col, c);
        return NULL;
    }

    /* NEWLINE + EOF sentinels, matching the reference lexer */
    if (append_token(out, make_token(K_NEWLINE,
            PyUnicode_FromString("\\n"), line, 0)) < 0) {
        Py_DECREF(out);
        return NULL;
    }
    if (append_token(out, make_token(K_EOF,
            PyUnicode_FromString(""), line, 0)) < 0) {
        Py_DECREF(out);
        return NULL;
    }
    return out;
}

static PyMethodDef IrlNativeMethods[] = {
    {"lex_fast", irl_lex_fast, METH_VARARGS,
     "lex_fast(source) -> [(kind, value, line, col), ...] — native tokenizer."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef irl_native_module = {
    PyModuleDef_HEAD_INIT, "_irl_native",
    "IRL™ native accelerator core (compiled machine code).",
    -1, IrlNativeMethods,
};

PyMODINIT_FUNC
PyInit__irl_native(void)
{
    for (int k = 0; k < NKINDS; k++) {
        KIND[k] = PyUnicode_InternFromString(KIND_NAMES[k]);
        if (KIND[k] == NULL) {
            return NULL;
        }
    }
    return PyModule_Create(&irl_native_module);
}
