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

"""Static validation for .irl source — the CI/CD and AI-friendly entry.

`check_source` never executes anything: it lexes and parses, and returns
machine-readable diagnostics. `irl lang check file.irl --json` prints the
same structure, so GitHub Actions and LLM agents can consume it directly.
"""

from .lexer import IrlSyntaxError, lex
from .parser import parse


def check_source(code):
    """Return {"ok": bool, "errors": [{line, column, message}]}."""
    errors = []
    try:
        parse(lex(code))
    except IrlSyntaxError as exc:
        errors.append(
            {
                "line": exc.line,
                "column": exc.column,
                "message": str(exc).split(": ", 1)[-1],
            }
        )
    except RecursionError:
        errors.append({"line": 0, "column": 0, "message": "expression nested too deeply"})
    return {"ok": not errors, "errors": errors}
