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

"""``irl lang`` — the .irl toy language, finally shipped with the package.

  irl lang run <file.irl>   execute a file
  irl lang demo             run the bundled demo program
  irl lang repl             interactive loop with a persistent brain
"""

import os
import sys

from rich.console import Console

from irl.lang import Interpreter, IrlRuntimeError, evaluate, lex, parse
from irl.lang.lexer import IrlSyntaxError

console = Console()

DEMO_PATH = os.path.join(os.path.dirname(__file__), "lang", "demo.irl")


def run_file(path):
    if not os.path.exists(path):
        console.print(f"[red]☠ The file '{path}' literally doesn't exist.[/red]")
        return 1
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()
    try:
        evaluate(parse(lex(code)))
        return 0
    except (IrlSyntaxError, IrlRuntimeError) as e:
        console.print(f"[red]{e}[/red]")
        return 1
    except Exception as e:
        console.print(f"[red][IRL_CRITICAL] ☠ Something went catastrophically wrong: {e}[/red]")
        return 1


def run_demo():
    console.print("[bold cyan]Running the bundled demo.irl ...[/bold cyan]\n")
    return run_file(DEMO_PATH)


def repl():
    """Statement-level REPL with a persistent environment.

    Blank line executes the buffered snippet, so multi-line `task`
    definitions behave. `exit` or Ctrl-D leaves. Ctrl-C clears the buffer.
    """
    from rich.panel import Panel

    console.print(Panel(
        "[bold]IRL™ Lang REPL[/bold] — snag/spill/bet/cap/grind/brb/task/fax/fake/fr/nah\n"
        "[dim]Blank line = run. `exit` = leave. Ctrl-C = clear buffer.[/dim]",
        border_style="cyan",
    ))
    interpreter = Interpreter()
    buffer = []

    while True:
        prompt = "irl>>> " if not buffer else "  ... "
        try:
            line = input(prompt)
        except EOFError:
            console.print("\n[dim]bet. later.[/dim]")
            break
        except KeyboardInterrupt:
            buffer = []
            console.print("\n[yellow]buffer cleared[/yellow]")
            continue

        if line.strip() in ("exit", "quit", "brb"):
            console.print("[dim]bet. later.[/dim]")
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


def run_lang(action, file=None):
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
    console.print("[red]Unknown lang action. Try: run | demo | repl[/red]")
    return 1
