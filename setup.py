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

"""Setuptools shim: builds the native accelerator when a C compiler exists.

The extension is optional — if compilation fails (no compiler, odd
platform), the wheel installs anyway and the pure-Python lexer runs.
CI (cibuildwheel) produces the prebuilt platform wheels.
"""

from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            "irl._irl_native",
            sources=["native/_irl_native.c"],
            extra_compile_args=["-O2"],
            optional=True,
        )
    ]
)
