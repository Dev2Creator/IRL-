"""The .irl language 2.1 — lexer/parser/interpreter/compiler parity suite.

Every behavioral claim of LANG.md is a test here. Legacy-slang programs
run through the same pipeline (alias parity). The compiler backend must
produce byte-identical output for the same programs (compiled parity).
"""

import io
import subprocess
import sys

import pytest

from irl.lang import Interpreter, evaluate, lex, parse
from irl.lang.builder import compile_source
from irl.lang.checker import check_source
from irl.lang.interpreter import IrlRuntimeError
from irl.lang.lexer import IrlSyntaxError


def run(code, **kwargs):
    return evaluate(parse(lex(code)), **kwargs)


def run_out(code, **kwargs):
    """Run and return captured stdout."""
    import contextlib

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        run(code, **kwargs)
    return buf.getvalue()


# ---------------------------------------------------------------- basics


def test_var_and_print(capsys):
    run("var x = 1\nprint(x + 41)")
    assert "42" in capsys.readouterr().out


def test_optional_semicolons_both_styles(capsys):
    run("var a = 5; print(a);")
    run("var b = 6\nprint(b)")
    out = capsys.readouterr().out
    assert "5" in out and "6" in out


def test_arithmetic_full_precedence(capsys):
    run("print((2 + 3) * 4, 2 ** 10, 10 / 4, -5 + 1, +7)")
    out = capsys.readouterr().out
    assert "20" in out and "1024" in out and "2.5" in out and "-4" in out


def test_hash_and_slash_comments():
    tokens = lex("# hash comment\n// slash comment\nvar x = 1")
    assert [t.value for t in tokens if t.type == "IDENT"] == ["x"]


def test_floats_and_escapes(capsys):
    run('var pi = 3.14\nprint(pi * 2, "line1\\nline2\\tend")')
    out = capsys.readouterr().out
    assert "6.28" in out and "line2" in out


def test_fstrings(capsys):
    run('var name = "Anika"\nvar age = 24\nprint(f"{name} is {age + 1} next year")')
    assert "Anika is 25 next year" in capsys.readouterr().out


def test_fstring_double_braces(capsys):
    run(r'print(f"literal {{braces}} and value {1 + 1}")')
    out = capsys.readouterr().out
    assert "literal {braces} and value 2" in out


# ---------------------------------------------------------------- control flow


def test_if_elif_else_chain(capsys):
    code = 'var n = 13\nif (n > 18) { print("adult") } elif (n > 12) { print("teen") } else { print("kid") }'
    run(code)
    assert "teen" in capsys.readouterr().out


def test_while_and_break_continue(capsys):
    code = "var i = 0\nwhile (true) {\n    i = i + 1\n    if (i == 2) { continue }\n    if (i == 5) { break }\n    print(i)\n}"
    out = run_out(code)
    assert "1" in out and "3" in out and "4" in out
    assert "2" not in out.split() and "5" not in out.split()


def test_for_in_lists_dicts_strings_ranges(capsys):
    run("for (x in [10, 20]) { print(x) }")
    run('for (k in {"a": 1}.keys()) { print(k) }')
    run('for (c in "hi") { print(c) }')
    run("for (i in range(2)) { print(i) }")
    out = capsys.readouterr().out
    for expected in ("10", "20", "a", "h", "i", "0", "1"):
        assert expected in out


# ---------------------------------------------------------------- data types


def test_dicts_index_assign_methods(capsys):
    code = 'var d = {"a": 1}\nd["b"] = 2\nprint(d["b"], len(d), d.keys(), d.values())'
    out = run_out(code)
    assert "2" in out and "2" in out and "'a'" in out and "1" in out


def test_lists_slice_negative_in(capsys):
    run("var n = [1, 2, 3, 4]\nprint(n[1:3], n[-1], 4 in n, 9 not in n)")
    out = capsys.readouterr().out
    assert "[2, 3]" in out and "4" in out and "True" in out


def test_string_methods(capsys):
    run('print("hi".upper(), "A,B".split(","), " x ".strip(), "aaa".count("a"))')
    out = capsys.readouterr().out
    assert "HI" in out and "['A', 'B']" in out and "x" in out and "3" in out


def test_none_literal(capsys):
    run("var z = none\nprint(z, type(z))")
    assert "None <class 'NoneType'>" in capsys.readouterr().out


# ---------------------------------------------------------------- functions


def test_functions_and_return(capsys):
    code = 'function greet(name) {\n    return "hello " + name\n}\nprint(greet("world"))'
    run(code)
    assert "hello world" in capsys.readouterr().out


def test_def_and_fn_aliases_work(capsys):
    run("def a(x) { return x }\nfn b(x) { return x * 2 }\nprint(a(3), b(3))")
    assert "3 6" in capsys.readouterr().out


def test_memo_function(capsys):
    code = "memo function fib(n) {\n    if (n < 2) { return n }\n    return fib(n - 1) + fib(n - 2)\n}\nprint(fib(90))"
    run(code)
    assert "2880067194370816120" in capsys.readouterr().out


def test_memo_with_unhashable_args_does_not_crash(capsys):
    code = "memo function first(items) { return items[0] }\nprint(first([7, 8]))"
    assert "7" in run_out(code)


def test_recursion_limit_is_friendly():
    code = "function boom(n) { return boom(n + 1) }\nboom(0)"
    with pytest.raises(IrlRuntimeError, match="Recursion went"):
        run(code)


# ---------------------------------------------------------------- types


def test_type_prints_like_python(capsys):
    run('print(type(1), type(1.5), type("s"), type(true), type([1]), type({"a": 1}))')
    out = capsys.readouterr().out
    for expected in (
        "<class 'int'>",
        "<class 'float'>",
        "<class 'str'>",
        "<class 'bool'>",
        "<class 'list'>",
        "<class 'dict'>",
    ):
        assert expected in out


def test_types_comparable_and_isinstance(capsys):
    run('print(type(1) == int, type("s") == str, isinstance(1.5, float))')
    assert "True True True" in capsys.readouterr().out


def test_print_sep_end(capsys):
    run('print(1, 2, sep=" | ", end="!\\n")')
    assert "1 | 2!" in capsys.readouterr().out


# ---------------------------------------------------------------- imports


def test_stdlib_import_allowlist(capsys):
    run("import math\nprint(math.sqrt(16), math.pi > 3)")
    out = capsys.readouterr().out
    assert "4.0" in out and "True" in out


def test_unknown_module_rejected():
    with pytest.raises(IrlRuntimeError, match="not available"):
        run("import socket")


def test_local_module_import(tmp_path):
    (tmp_path / "utils.irl").write_text("var magic = 42\nfunction double(x) { return x * 2 }\n")
    code = 'import "utils.irl"\nprint(magic, double(21))'
    assert "42 42" in run_out(code, source_dir=str(tmp_path))


# ---------------------------------------------------------------- legacy alias parity


def test_legacy_slang_runs_on_21(capsys):
    code = 'task greet(name) {\n    brb "hello " + name;\n}\nsnag n = 10;\nbet (n > 5) { spill(greet("world")); } cap { spill("small"); }\nsnag arr = ["a", "b"];\npush(arr, "c");\nspill(len(arr));'
    out = run_out(code)
    assert "hello world" in out and "3" in out


def test_old_spill_is_plain_output_now(capsys):
    """The 2.0 💦 prefix is gone in the professional edition."""
    run('spill("plain now")')
    out = capsys.readouterr().out
    assert "plain now" in out and "💦" not in out


# ---------------------------------------------------------------- errors


def test_syntax_error_has_position():
    with pytest.raises(IrlSyntaxError) as excinfo:
        run("var = 5")
    assert excinfo.value.line >= 1


def test_runtime_error_clean_not_traceback():
    with pytest.raises(IrlRuntimeError, match="not defined"):
        run("print(ghost)")


def test_error_format_caret():
    from irl.lang_runner import format_error

    try:
        parse(lex("var = 5\n"))
        raised = None
    except IrlSyntaxError as exc:
        raised = exc
    assert raised is not None
    rendered = format_error(raised, "var = 5\n")
    assert "^" in rendered


# ---------------------------------------------------------------- builtins table


def test_interpreter_builtin_table():
    interp = Interpreter()
    for name in ("print", "input", "int", "float", "str", "len", "range", "sum", "min", "max", "abs", "round", "sorted", "type", "isinstance", "append"):
        assert callable(interp.global_env.get(name))


# ---------------------------------------------------------------- checker & spec


def test_check_source_clean():
    assert check_source("var x = 1\nprint(x)")["ok"] is True


def test_check_source_error_schema():
    payload = check_source("var = 5")
    assert payload["ok"] is False
    err = payload["errors"][0]
    assert set(err) == {"line", "column", "message"}
    assert err["line"] >= 1


def test_spec_exports():
    from irl.lang.spec import GRAMMAR_EBNF, KEYWORD_TABLE

    assert "var_decl" in GRAMMAR_EBNF
    assert "print()" in KEYWORD_TABLE


# ---------------------------------------------------------------- compiler


def test_compile_source_is_valid_python():
    py_source, _ = compile_source("var x = 2\nprint(x * 21)")
    compile(py_source, "<test>", "exec")  # raises on invalid Python


def test_constant_folding_and_report():
    py_source, report = compile_source("var x = 2 + 3 * 4\nprint(x)")
    assert report["constants_folded"] >= 1
    assert "14" in py_source  # folded at build time


def test_dead_code_elimination():
    _, report = compile_source('if (false) { print("no") }\nprint("yes")')
    assert report["dead_branches_removed"] >= 1


def test_builtin_caching_at_o2():
    py_source, _ = compile_source("print(len([1, 2]))", level=2)
    assert "_irl_print" in py_source and "_irl_len" in py_source


def test_compiled_parity_with_interpreter(tmp_path):
    """Same program, both backends, identical stdout."""
    programs = [
        "var t = 0\nfor (i in range(5)) {\n    t = t + i * 2\n}\nprint(t)",
        "memo function sq(x) { return x * x }\nprint(sq(9), sq(12))",
        'var d = {"k": 1}\nd["m"] = 2\nprint(d.keys(), sum([1, 2, 3]), 3 ** 2)',
    ]
    for i, src in enumerate(programs):
        import contextlib

        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            run(src)
        interpreted_out = buf.getvalue()

        py_source, _ = compile_source(src, level=2)
        py_file = tmp_path / f"prog{i}.py"
        py_file.write_text(py_source)
        compiled_out = subprocess.run(
            [sys.executable, str(py_file)],
            capture_output=True,
            text=True,
            timeout=60,
        ).stdout
        assert compiled_out == interpreted_out, f"parity failed for program {i}"


def test_build_cli_end_to_end(tmp_path):
    src = tmp_path / "app.irl"
    src.write_text('var x = 6\nprint("answer", x * 7)\n')
    from irl.lang.builder import build_file

    rc = build_file(str(src), ["-O2"])
    assert rc == 0
    pyc = tmp_path / "app.pyc"
    assert pyc.exists()
    result = subprocess.run([sys.executable, str(pyc)], capture_output=True, text=True, timeout=60)
    assert "answer 42" in result.stdout


def test_build_rejects_unknown_module():
    with pytest.raises(Exception):
        compile_source('import socket\nprint("nope")')
