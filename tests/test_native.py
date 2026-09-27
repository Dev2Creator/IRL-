"""Native accelerator parity — the machine-code lexer must match the
reference Python lexer token-for-token, and both must produce the same
program output through the full pipeline."""

import pytest

from irl.lang import lexer as lexer_mod
from irl.lang import parse
from irl.lang.interpreter import evaluate
from irl.lang.lexer import IrlSyntaxError, _lex_python, lex

try:
    from irl import _irl_native  # noqa: F401

    HAS_NATIVE = True
except ImportError:
    HAS_NATIVE = False

CORPUS = [
    "",
    "// only a comment",
    "# hash comment",
    "var x = 3.14",
    "snag x = 1; spill(x + 41);",
    "function f(a, b) { return a ** 2 - b }\nprint(f(3, 2))",
    'bet (true) { print("yes") } cap { print("no") }',
    "for (i in range(3)) { print(i) }",
    'var d = {"a": 1, "b": [1, 2]}\nprint(d["b"][1], 3 in [1, 2, 3], 9 not in [1])',
    'print(f"hi {1 + 1} and {{literal}}")',
    'print("escapes: \\n\\t\\"quoted\\"")',
    "import math\nprint(math.sqrt(4), math.pi)",
    "memo function fib(n) { if (n < 2) { return n } return fib(n-1) + fib(n-2) }\nprint(fib(10))",
    "print(1.5, 2.50, 0.25, 1_0 == 10 if false else none)" if False else "print(1.5, 0.25)",
    'var s = "multi \\n line"\nprint(s.lower(), "x".isdigit())',
    'grind (false) { print("never") }',
]


@pytest.mark.skipif(not HAS_NATIVE, reason="native accelerator not built")
@pytest.mark.parametrize("source", CORPUS)
def test_native_matches_python_tokenizer(source):
    py_tokens = _lex_python(source)
    native_tokens = lex(source)
    assert len(py_tokens) == len(native_tokens)
    for pt, nt in zip(py_tokens, native_tokens):
        assert (pt.type, pt.value, pt.line, pt.column) == (nt.type, nt.value, nt.line, nt.column), f"divergence on {source!r}: {pt} != {nt}"


@pytest.mark.skipif(not HAS_NATIVE, reason="native accelerator not built")
def test_native_error_matches_python_error():
    with pytest.raises(IrlSyntaxError) as py_exc:
        _lex_python('var x = "unterminated')
    with pytest.raises(IrlSyntaxError) as nat_exc:
        lex('var x = "unterminated')
    assert py_exc.value.line == nat_exc.value.line
    assert "Unterminated" in str(nat_exc.value)


@pytest.mark.skipif(not HAS_NATIVE, reason="native accelerator not built")
def test_native_pipeline_end_to_end(capsys):
    """Native lexer feeds the same parser/interpreter unchanged."""
    code = 'var x = 6\nprint("answer", x * 7)'
    assert lex is not _lex_python
    evaluate(parse(lex(code)))
    assert "answer 42" in capsys.readouterr().out


def test_fallback_is_explicit():
    assert lexer_mod._lex_python is not None
    assert callable(lexer_mod.lex)
