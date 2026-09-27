"""IRL language lexer — 2.1 "Full Language Edition".

Standard keywords (with legacy slang aliases), floats, string escapes,
f-strings, ** power, # and // comments, significant NEWLINEs.
"""

import re
from dataclasses import dataclass
from typing import List


@dataclass
class Token:
    type: str
    value: object
    line: int
    column: int


class IrlSyntaxError(Exception):
    def __init__(self, message, line, column):
        self.line = line
        self.column = column
        super().__init__(f"[IRL_ERROR] line {line}, col {column}: {message}")


# Canonical keywords: the statement/operator words of the language.
KEYWORDS = {
    "var",
    "function",
    "if",
    "elif",
    "else",
    "while",
    "for",
    "in",
    "break",
    "continue",
    "return",
    "true",
    "false",
    "none",
    "memo",
    "import",
    "and",
    "or",
    "not",
}

# Every accepted spelling -> canonical keyword or builtin identifier.
# Legacy slang (snag/spill/bet/cap/grind/brb/task/fax/fake/fr/nah) maps
# onto the standard names so old programs keep running.
WORD_ALIASES = {
    "var": "var",
    "let": "var",
    "function": "function",
    "def": "function",
    "fn": "function",
    "if": "if",
    "elif": "elif",
    "else": "else",
    "while": "while",
    "for": "for",
    "in": "in",
    "break": "break",
    "continue": "continue",
    "return": "return",
    "true": "true",
    "false": "false",
    "none": "none",
    "memo": "memo",
    "import": "import",
    "and": "and",
    "or": "or",
    "not": "not",
    # legacy slang -> standard names
    "snag": "var",
    "bet": "if",
    "cap": "else",
    "grind": "while",
    "brb": "return",
    "task": "function",
    "fax": "true",
    "fake": "false",
    "fr": "and",
    "nah": "not",
    # builtins that were once keywords / had other names
    "spill": "print",
    "ask": "input",
    "push": "append",
}

ESCAPES = {
    "n": "\n",
    "t": "\t",
    "r": "\r",
    "0": "\0",
    '"': '"',
    "\\": "\\",
    "{": "{",
    "}": "}",
}


def unescape(raw: str) -> str:
    out = []
    i = 0
    while i < len(raw):
        ch = raw[i]
        if ch == "\\" and i + 1 < len(raw):
            out.append(ESCAPES.get(raw[i + 1], "\\" + raw[i + 1]))
            i += 2
        else:
            out.append(ch)
            i += 1
    return "".join(out)


TOKEN_SPEC = [
    ("COMMENT", r"//[^\n]*|#[^\n]*"),
    ("FSTRING", r'f"(?:\\.|[^"\\])*"'),
    ("STRING", r'"(?:\\.|[^"\\])*"'),
    ("NUMBER", r"\d+\.\d+|\d+"),
    ("POWER", r"\*\*"),
    ("EQEQ", r"=="),
    ("NEQ", r"!="),
    ("LTE", r"<="),
    ("GTE", r">="),
    ("ASSIGN", r"="),
    ("LT", r"<"),
    ("GT", r">"),
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("MUL", r"\*"),
    ("DIV", r"/"),
    ("SEMI", r";"),
    ("COMMA", r","),
    ("COLON", r":"),
    ("DOT", r"\."),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("LBRACE", r"\{"),
    ("RBRACE", r"\}"),
    ("LBRACKET", r"\["),
    ("RBRACKET", r"\]"),
    ("NEWLINE", r"\n"),
    ("SKIP", r"[ \t\r]+"),
    ("NAME", r"[a-zA-Z_]\w*"),
    ("MISMATCH", r"."),
]

tok_regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC)
get_token = re.compile(tok_regex).match

try:  # native accelerator (compiled machine code); pure-Python fallback
    from .. import _irl_native
except ImportError:  # pragma: no cover - pure wheels and non-native builds
    _irl_native = None


def _lex_python(code: str) -> List[Token]:
    line_num = 1
    line_start = 0
    tokens: List[Token] = []
    mo = get_token(code)

    while mo is not None:
        kind = mo.lastgroup
        value = mo.group(kind)
        column = mo.start() - line_start + 1

        if kind == "NEWLINE":
            line_start = mo.end()
            line_num += 1
            tokens.append(Token("NEWLINE", "\\n", line_num - 1, column))
        elif kind in ("SKIP", "COMMENT"):
            pass
        elif kind == "MISMATCH":
            raise IrlSyntaxError(f"Unexpected character '{value}'.", line_num, column)
        elif kind == "NAME":
            canonical = WORD_ALIASES.get(value)
            if canonical is not None:
                if canonical in KEYWORDS:
                    tokens.append(Token("KEYWORD", canonical, line_num, column))
                else:
                    tokens.append(Token("IDENT", canonical, line_num, column))
            else:
                tokens.append(Token("IDENT", value, line_num, column))
        elif kind == "STRING":
            tokens.append(Token("STRING", unescape(value[1:-1]), line_num, column))
        elif kind == "FSTRING":
            tokens.append(Token("FSTRING", value[2:-1], line_num, column))
        elif kind == "NUMBER":
            tokens.append(Token("NUMBER", value, line_num, column))
        else:
            tokens.append(Token(kind, value, line_num, column))

        mo = get_token(code, mo.end())

    tokens.append(Token("NEWLINE", "\\n", line_num, 0))
    tokens.append(Token("EOF", "", line_num, 0))
    return tokens


def _lex_native(code: str) -> List[Token]:
    """Native machine-code tokenizer; same stream as _lex_python."""
    try:
        raw = _irl_native.lex_fast(code)
    except ValueError as exc:
        message = str(exc)
        # error protocol: \x01line\x01col\x01text
        parts = message.split("\x01")
        if len(parts) == 4:
            raise IrlSyntaxError(parts[3], int(parts[1]), int(parts[2]))
        raise IrlSyntaxError(message, 1, 1)
    return [Token(kind, value, line, col) for kind, value, line, col in raw]


def lex(code: str) -> List[Token]:
    if _irl_native is not None:
        return _lex_native(code)
    return _lex_python(code)
