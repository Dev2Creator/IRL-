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

"""Setuptools shim: builds the native accelerator for native wheels.

The C core is compiled ONLY for the prebuilt platform wheels
(cibuildwheel sets CIBUILDWHEEL=1) or on explicit request
(IRL_BUILD_NATIVE=1 — local dev). Everything else — pip install from
sdist, the PyPI release build — ships pure Python with the fallback
lexer, so the release wheel stays universal and PyPI never sees a bare
linux_x86_64 platform tag. If compilation fails, the build continues
pure (the extension is optional).
"""

import os
import sys

from setuptools import Extension, setup

NATIVE_REQUESTED = (
    os.environ.get("CIBUILDWHEEL") == "1"
    or os.environ.get("IRL_BUILD_NATIVE") == "1"
)

if NATIVE_REQUESTED:
    flags = ["/O2"] if sys.platform == "win32" else ["-O2"]
    ext_modules = [
        Extension(
            "irl._irl_native",
            sources=["native/_irl_native.c"],
            extra_compile_args=flags,
            optional=True,
        )
    ]
else:
    ext_modules = []

setup(ext_modules=ext_modules)
