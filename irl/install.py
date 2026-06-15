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
from irl.state import add_coins

def check_registry(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        response = requests.get(url, headers=headers, timeout=10)
        return response.status_code == 200
    except Exception:
        return False

def install_package(target):
    from irl.themes import get_engine
    engine = get_engine()
    
    engine.render_install_start(target)

    # Direct URL
    if target.startswith("http://") or target.startswith("https://"):
        download_and_extract(target)
        add_coins(10, "Installed a package")
        engine.render_install_success(target)
        return

    # GitHub format user/repo
    if "/" in target and not target.startswith("@"):
        url = f"https://github.com/{target}/archive/refs/heads/main.zip"
        download_and_extract(url)
        add_coins(10, "Installed a package")
        engine.render_install_success(target)
        return

    # Check PyPI
    if check_registry(f"https://pypi.org/pypi/{target}/json"):
        install_pip(target)
        add_coins(10, "Installed a package")
        engine.render_install_success(target)
        return

    # Check NPM
    if check_registry(f"https://registry.npmjs.org/{target}"):
        install_npm(target)
        add_coins(10, "Installed a package")
        engine.render_install_success(target)
        return

    # Fallback to GitHub Keyword Search
    try:
        search_url = f"https://api.github.com/search/repositories?q={target}&sort=stars&order=desc"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        response = requests.get(search_url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            items = data.get("items", [])
            if items:
                best_match = items[0]
                repo_full_name = best_match.get("full_name", target)
                default_branch = best_match.get("default_branch", "main")
                
                zip_url = f"https://github.com/{repo_full_name}/archive/refs/heads/{default_branch}.zip"
                download_and_extract(zip_url)
                add_coins(10, "Installed a package")
                engine.render_install_success(target)
                return
    except Exception as e:
        pass

    engine.ui.render_generic(f"✖ Error: Package or keyword '{target}' not found on NPM, PyPI, or GitHub.")

def upgrade_irl():
    from irl.console import console
    import subprocess
    import sys
    console.print("\n[bold cyan]Upgrading IRL™ OS...[/bold cyan]")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "irl-pkg"])
        console.print("[bold green]✨ IRL™ OS successfully upgraded to the latest version! ✨[/bold green]")
    except subprocess.CalledProcessError:
        console.print("[bold red]Failed to upgrade IRL™ OS. Check your permissions or internet connection.[/bold red]")
