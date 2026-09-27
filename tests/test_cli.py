"""CLI smoke: every subcommand answers --help, easter eggs fire, dashboard
degrades gracefully without a TTY."""

import sys

import pytest

SUBCOMMANDS = [
    "install",
    "glasses",
    "doctor",
    "grass",
    "posture",
    "window",
    "mirror",
    "hydrate",
    "chaos",
    "store",
    "games",
    "city",
    "search",
    "upgrade",
    "rollback",
    "run",
    "manga",
    "story",
    "bones",
    "joke",
    "dog",
    "dashboard",
    "dash",
    "tui",
    "pet",
    "achievements",
    "quests",
    "grassland",
    "rhythm",
    "lang",
]


def run_cli(argv, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["irl", *argv])
    from irl.main import cli

    cli()


@pytest.mark.parametrize("command", SUBCOMMANDS)
def test_every_subcommand_has_help(command, monkeypatch, capsys):
    with pytest.raises(SystemExit) as exc:
        run_cli([command, "--help"], monkeypatch)
    assert exc.value.code == 0
    out = capsys.readouterr().out
    assert command in out or "Usage" in out or "usage" in out


def test_top_level_help_lists_commands(monkeypatch, capsys, seed_state):
    run_cli(["-h"], monkeypatch)
    out = capsys.readouterr().out
    for expected in ("install", "doctor", "rollback", "grassland", "rhythm", "pet"):
        assert expected in out.lower()


def test_egg_42(monkeypatch, capsys, seed_state):
    run_cli(["42"], monkeypatch)
    out = capsys.readouterr().out
    assert "42" in out
    assert "Life" in out or "life" in out


def test_egg_pizza(monkeypatch, capsys, seed_state):
    run_cli(["pizza"], monkeypatch)
    out = capsys.readouterr().out
    assert "pizza delivery" in out.lower() or "Mamma mia" in out


def test_egg_42_unlocks_matrix(monkeypatch, capsys, seed_state):
    run_cli(["42"], monkeypatch)
    from irl.state import load_state

    assert "matrix" in load_state().get("unlocked_themes", [])


def test_dashboard_compact_mode_piped(monkeypatch, capsys, seed_state):
    """Without a TTY the dashboard offers a numbered menu instead of crashing."""
    responses = iter(["0"])
    monkeypatch.setattr("builtins.input", lambda *a, **kw: next(responses))
    run_cli(["dashboard"], monkeypatch)
    out = capsys.readouterr().out
    assert "Dashboard" in out or "dashboard" in out


def test_lang_demo(capsys, monkeypatch):
    import io

    monkeypatch.setattr("sys.stdin", io.StringIO("Anika\n"))
    run_cli(["lang", "demo"], monkeypatch)
    assert "fib(30)" in capsys.readouterr().out


def test_quests_board_renders(capsys, monkeypatch, seed_state):
    run_cli(["quests"], monkeypatch)
    out = capsys.readouterr().out
    assert "QUESTS" in out.upper()


def test_achievements_board_renders(capsys, monkeypatch, seed_state):
    run_cli(["achievements"], monkeypatch)
    out = capsys.readouterr().out
    assert "Achievement" in out or "Noob" in out


def test_beautiful_failure_not_raw_traceback(monkeypatch, capsys, seed_state):
    """A command that explodes shows the styled panel, not a stack trace."""
    monkeypatch.setattr("irl.main.install_package", lambda pkg: (_ for _ in ()).throw(RuntimeError("boom")))
    with pytest.raises(SystemExit) as exc:
        run_cli(["install", "requests"], monkeypatch)
    assert exc.value.code == 1
    out = capsys.readouterr().out
    assert "Traceback" not in out
    assert "boom" in out
    assert "irl doctor" in out
