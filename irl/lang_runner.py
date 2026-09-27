# IRL™ 🌱 - Software for Humans
# Copyright (C) 2026 Anika Mukherjee
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""``irl lang`` — the .irl language, 2.1 "Full Language Edition".

irl lang run <file.irl>        execute a file (interpreter)
irl lang build <file.irl>      compile to Python bytecode (.pyc)
irl lang check <file.irl>      validate without running (--json for CI/AI)
irl lang spec [--json]         print the language grammar (EBNF)
irl lang bench                 interpreter vs compiled vs CPython benchmarks
irl lang demo                  run the bundled demo program
irl lang repl                  interactive loop with a persistent kernel
"""

import json as _json
import os

from rich.console import Console

from irl.lang import Interpreter, IrlRuntimeError, evaluate, lex, parse
from irl.lang.lexer import IrlSyntaxError

console = Console()

DEMO_PATH = os.path.join(os.path.dirname(__file__), "lang", "demo.irl")


def read_source(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def format_error(exc, code=None):
    """Render an IRL error with a caret pointing at the problem."""
    line_no = getattr(exc, "line", None)
    col = getattr(exc, "column", None)
    text = str(exc)
    if line_no is None or code is None:
        return text
    lines = code.splitlines()
    if not (1 <= line_no <= len(lines)):
        return text
    src = lines[line_no - 1]
    caret_col = col if isinstance(col, int) and col > 0 else 1
    caret = " " * (caret_col - 1) + "^"
    return f"{text}\n      {src}\n      {caret}"


def run_file(path):
    if not os.path.exists(path):
        console.print(f"[red][IRL_ERROR] The file '{path}' doesn't exist.[/red]")
        return 1
    code = read_source(path)
    source_dir = os.path.dirname(os.path.abspath(path))
    try:
        evaluate(parse(lex(code)), source_dir=source_dir)
        return 0
    except (IrlSyntaxError, IrlRuntimeError) as e:
        console.print(f"[red]{format_error(e, code)}[/red]")
        return 1
    except Exception as e:
        console.print(f"[red][IRL_CRITICAL] Something went catastrophically wrong: {e}[/red]")
        return 1


def run_demo():
    console.print("[bold cyan]Running the bundled demo.irl ...[/bold cyan]\n")
    return run_file(DEMO_PATH)


def repl():
    """Statement-level REPL with a persistent kernel.

    Blank line executes the buffered snippet, so multi-line `function`
    definitions behave. `exit` or Ctrl-D leaves. Ctrl-C clears the buffer.
    """
    from rich.panel import Panel

    console.print(
        Panel(
            "[bold]IRL™ Lang REPL 2.1[/bold] — var/print/function/if/elif/while/for/memo/import\n[dim]Blank line = run. `exit` = leave. Ctrl-C = clear buffer. Legacy slang still works.[/dim]",
            border_style="cyan",
        )
    )
    interpreter = Interpreter()
    buffer = []

    while True:
        prompt = "irl>>> " if not buffer else "  ... "
        try:
            line = input(prompt)
        except EOFError:
            console.print("\n[dim]later.[/dim]")
            break
        except KeyboardInterrupt:
            buffer = []
            console.print("\n[yellow]buffer cleared[/yellow]")
            continue

        if line.strip() in ("exit", "quit"):
            console.print("[dim]later.[/dim]")
            break
        if not line.strip():
            if not buffer:
                continue
            code = "\n".join(buffer)
            buffer = []
            try:
                result = interpreter.interpret(parse(lex(code)))
                if result is not None:
                    print(repr(result))
            except (IrlSyntaxError, IrlRuntimeError) as e:
                console.print(f"[red]{e}[/red]")
            except Exception as e:
                console.print(f"[red]☠ {e}[/red]")
            continue
        buffer.append(line)


def check_file(path, as_json=False):
    """Validate a .irl file without running it. Exit code 0 = clean."""
    from irl.lang.checker import check_source

    if not os.path.exists(path):
        payload = {
            "ok": False,
            "file": path,
            "errors": [{"line": 0, "column": 0, "message": f"file not found: {path}"}],
        }
        if as_json:
            print(_json.dumps(payload, indent=2))
        else:
            console.print(f"[red][IRL_ERROR] {path}: file not found[/red]")
        return 1

    code = read_source(path)
    payload = check_source(code)
    payload["file"] = path
    if as_json:
        print(_json.dumps(payload, indent=2))
    elif payload["ok"]:
        console.print(f"[green]✔ {path}: no syntax errors[/green]")
    else:
        for err in payload["errors"]:
            console.print(f"[red][IRL_ERROR] line {err['line']}, col {err['column']}: {err['message']}[/red]")
        console.print(f"[red]{path}: {len(payload['errors'])} error(s)[/red]")
    return 0 if payload["ok"] else 1


def print_spec(as_json=False):
    from irl.lang.spec import GRAMMAR_EBNF, KEYWORD_TABLE

    if as_json:
        print(_json.dumps({"grammar_ebnf": GRAMMAR_EBNF, "keywords": KEYWORD_TABLE}, indent=2))
        return 0
    console.print("[bold cyan]IRL™ Language 2.1 — Grammar (EBNF)[/bold cyan]\n")
    console.print(GRAMMAR_EBNF)
    console.print("\n[bold]Keywords (canonical + accepted aliases):[/bold]")
    for canonical, spellings in KEYWORD_TABLE.items():
        console.print(f"  [green]{canonical}[/green]: {', '.join(spellings)}")
    return 0


def run_lang(action, file=None, build_args=None):
    if action == "run":
        if not file:
            console.print("[red]Usage: irl lang run <file.irl>[/red]")
            return 1
        return run_file(file)
    if action == "demo":
        return run_demo()
    if action == "repl":
        repl()
        return 0
    if action == "check":
        if not file:
            console.print("[red]Usage: irl lang check <file.irl> [--json][/red]")
            return 1
        as_json = "--json" in (build_args or [])
        return check_file(file, as_json=as_json)
    if action == "spec":
        return print_spec(as_json="--json" in (build_args or []))
    if action == "build":
        if not file:
            console.print("[red]Usage: irl lang build <file.irl> [-o out] [--run] [-O0|-O1|-O2] [--emit-ir] [--emit-py] [-v][/red]")
            return 1
        from irl.lang.builder import build_file

        return build_file(file, build_args or [])
    if action == "bench":
        from irl.lang.bench import run_bench

        return run_bench()
    console.print("[red]Unknown lang action. Try: run | build | check | spec | bench | demo | repl[/red]")
    return 1
