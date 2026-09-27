"""The .irl language: lex -> parse -> evaluate, plus the runner."""

import io

import pytest

from irl.lang import Interpreter, evaluate, lex, parse
from irl.lang.lexer import IrlSyntaxError


def run(code):
    return evaluate(parse(lex(code)))


def test_snag_and_spill(capsys):
    run("snag x = 1;\nspill(x + 41);")
    out = capsys.readouterr().out
    assert "42" in out


def test_basics_arithmetic(capsys):
    run("spill((2 + 3) * 4);")
    assert "20" in capsys.readouterr().out


def test_task_and_brb(capsys):
    code = 'task greet(name) {\n    brb "hello " + name;\n}\nspill(greet("world"));'
    run(code)
    assert "hello world" in capsys.readouterr().out


def test_bet_cap(capsys):
    code = 'snag n = 10;\nbet (n > 5) {\n    spill("big");\n} cap {\n    spill("small");\n}'
    run(code)
    assert "big" in capsys.readouterr().out


def test_grind_loop(capsys):
    code = "snag i = 0;\ngrind (i < 3) {\n    spill(i);\n    i = i + 1;\n}"
    run(code)
    out = capsys.readouterr().out
    assert out.count("0") >= 1 and "3" not in out


def test_arrays_and_builtins(capsys):
    code = 'snag arr = ["a", "b"];\npush(arr, "c");\nspill(len(arr));'
    run(code)
    assert "3" in capsys.readouterr().out


def test_truth_values_and_logic(capsys):
    """fax/fake drive bet-branches (bare expressions aren't statements)."""
    run('bet (fax) { spill("yes-branch"); }')
    assert "yes-branch" in capsys.readouterr().out
    run('bet (nah fax) { spill("wrong"); } cap { spill("cap-branch"); }')
    assert "cap-branch" in capsys.readouterr().out
    assert "wrong" not in capsys.readouterr().out


def test_syntax_error_is_snarky_not_fatal():
    with pytest.raises(IrlSyntaxError):
        run("spill oops")


def test_runner_runs_demo_file(capsys, monkeypatch):
    """The bundled demo.irl runs end-to-end when ask() gets input."""
    import irl.lang_runner as lr

    monkeypatch.setattr("sys.stdin", io.StringIO("Anika\n"))
    exit_code = lr.run_demo()
    out = capsys.readouterr().out
    assert exit_code == 0
    assert "3" in out  # the array-length spill
    assert "Anika" in out  # ask() captured stdin


def test_repl_persistent_environment(monkeypatch, capsys):
    """Definitions survive across REPL snippets."""
    import irl.lang_runner as lr

    responses = iter(["snag x = 40;\n", "spill(x + 2);\n", "", "exit"])
    monkeypatch.setattr("builtins.input", lambda *a, **kw: next(responses))
    lr.repl()
    assert "42" in capsys.readouterr().out


def test_interpreter_has_builtins():
    interp = Interpreter()
    assert interp.global_env.get("ask")
    assert interp.global_env.get("len")
    assert interp.global_env.get("push")
