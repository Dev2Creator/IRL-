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

"""The .irl toy language — snag/spill/bet/cap/grind/brb/task.

Exposed: lex, parse, evaluate, Interpreter, and the error types.
"""

from .lexer import lex, IrlSyntaxError
from .parser import parse
from .interpreter import evaluate, Interpreter, IrlRuntimeError

__all__ = ["lex", "parse", "evaluate", "Interpreter", "IrlSyntaxError", "IrlRuntimeError"]
