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
import json
from irl.console import console
import time

def format_size(size_in_bytes):
    if not size_in_bytes:
        return "Unknown"
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.1f} {unit}"
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.1f} TB"

def get_npm_info(package):
    url = f"https://registry.npmjs.org/{package}"
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            latest_version = data.get("dist-tags", {}).get("latest")
            if latest_version and latest_version in data.get("versions", {}):
                version_data = data["versions"][latest_version]
                size = version_data.get("dist", {}).get("unpackedSize")
                return {
                    "package": package,
                    "version": latest_version,
                    "size": format_size(size) if size else "Unknown (Tarball)",
                    "source": "NPM",
                    "install_method": "npm"
                }
    except:
        pass
    return None

def get_pypi_info(package):
    url = f"https://pypi.org/pypi/{package}/json"
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            version = data.get("info", {}).get("version", "Unknown")
            urls = data.get("urls", [])
            size = None
            if urls:
                for u in urls:
                    if u.get("packagetype") == "bdist_wheel":
                        size = u.get("size")
                        break
                if not size and urls:
                    size = urls[0].get("size")
                    
            return {
                "package": package,
                "version": version,
                "size": format_size(size) if size else "Unknown",
                "source": "PyPI",
                "install_method": "pip"
            }
    except:
        pass
    return None

def get_github_info(package):
    if "/" not in package or package.startswith("@"):
        return None
        
    url = f"https://api.github.com/repos/{package}"
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            size_kb = data.get("size", 0)
            return {
                "package": data.get("name", package),
                "version": data.get("default_branch", "main"),
                "size": format_size(size_kb * 1024) if size_kb else "Unknown",
                "source": "GitHub",
                "install_method": "Available"
            }
    except:
        pass
    return None

def inspect_package(package):
    console.print("\n[bold cyan]👓 Looking closely...[/bold cyan]\n")
    
    time.sleep(1)
    
    info = get_npm_info(package)
    if not info:
        info = get_pypi_info(package)
    if not info:
        info = get_github_info(package)
        
    if info:
        console.print(f"[bold]Package:[/bold] {info['package']}")
        console.print(f"[bold]Version:[/bold] {info['version']}")
        console.print(f"[bold]Size:[/bold] {info['size']}")
        console.print(f"[bold]Source:[/bold] {info['source']}")
        console.print(f"[bold]Install Method:[/bold] {info['install_method']}\n")
        console.print("[green]Vision enhanced.[/green]\n")
    else:
        console.print(f"[red]❌ Error:[/red] Package '{package}' not found on NPM, PyPI, or GitHub.")
        console.print("[yellow]Vision impaired.[/yellow]\n")
