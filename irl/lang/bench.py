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

"""`irl lang bench` — honest numbers, three engines.

Compares the .irl tree-walking interpreter, the compiled (CPython
bytecode) path, and plain hand-written CPython on identical programs.
"""

import time

from rich.console import Console
from rich.table import Table

from irl.lang import Interpreter, lex, parse
from irl.lang.builder import compile_source

console = Console()

FIB_SRC = """\
function fib(n) {
    if (n < 2) {
        return n
    }
    return fib(n - 1) + fib(n - 2)
}
print(fib(20))
"""

LOOP_SRC = """\
var total = 0
var i = 0
while (i < 200000) {
    total = total + i
    i = i + 1
}
print(total)
"""

FIB_PY = "def fib(n):\n    return n if n < 2 else fib(n - 1) + fib(n - 2)\nprint(fib(20))\n"
LOOP_PY = "total = 0\ni = 0\nwhile i < 200000:\n    total = total + i\n    i = i + 1\nprint(total)\n"


def _time(fn, runs=1):
    best = None
    for _ in range(runs):
        start = time.perf_counter()
        fn()
        elapsed = time.perf_counter() - start
        best = elapsed if best is None else min(best, elapsed)
    return best


def _run_interpreted(src):
    def go():
        Interpreter().interpret(parse(lex(src)))

    return go


def _run_compiled(src):
    py_source, _ = compile_source(src, level=2)
    namespace = {}
    code = compile(py_source, "<irl-compiled>", "exec")

    def go():
        exec(code, namespace)

    return go


def _run_python(src):
    code = compile(src, "<cpython>", "exec")
    namespace = {}

    def go():
        exec(code, namespace)

    return go


def run_bench():
    rows = []
    for name, irl_src, py_src, runs in (
        ("recursive fib(20)", FIB_SRC, FIB_PY, 3),
        ("while loop 200k", LOOP_SRC, LOOP_PY, 3),
    ):
        interp = _time(_run_interpreted(irl_src), runs)
        compiled = _time(_run_compiled(irl_src), runs)
        cpython = _time(_run_python(py_src), runs)
        rows.append((name, interp, compiled, cpython))

    table = Table(title="IRL™ Language Bench — lower is better", border_style="cyan")
    table.add_column("workload")
    table.add_column("interpreted", justify="right")
    table.add_column("compiled (IRL → CPython)", justify="right")
    table.add_column("plain CPython", justify="right")
    table.add_column("compiled vs CPython", justify="right")
    for name, interp, compiled, cpython in rows:
        ratio = f"{cpython / compiled:.2f}x" if compiled else "n/a"
        table.add_row(
            name,
            f"{interp * 1000:.1f} ms",
            f"{compiled * 1000:.1f} ms",
            f"{cpython * 1000:.1f} ms",
            ratio,
        )
    console.print(table)
    console.print(
        "[dim]Compiled IRL folds constants and caches builtins at build time, "
        "so it does less work per loop than the equivalent naive Python — "
        "a ratio above 1.00x means compiled .irl beat plain CPython.[/dim]"
    )
    return 0
