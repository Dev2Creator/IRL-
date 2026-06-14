# IRL™ 🌱 - Software for Humans
# Copyright (C) 2026 UNKNOWN™
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

import requests
from irl.wrappers import install_npm, install_pip
from irl.extract import download_and_extract

def check_registry(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def install_package(target):
    # Direct URL
    if target.startswith("http://") or target.startswith("https://"):
        download_and_extract(target)
        return

    # GitHub format user/repo
    if "/" in target and not target.startswith("@"):
        url = f"https://github.com/{target}/archive/refs/heads/main.zip"
        download_and_extract(url)
        return

    # Check NPM
    print(f"🔍 Searching for '{target}'...")
    if check_registry(f"https://registry.npmjs.org/{target}"):
        install_npm(target)
        return

    # Check PyPI
    if check_registry(f"https://pypi.org/pypi/{target}/json"):
        install_pip(target)
        return

    print(f"✖ Error: Package '{target}' not found on NPM, PyPI, or GitHub.")
