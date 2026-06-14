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

import shutil
import requests
import time
import subprocess
from rich.console import Console
from irl.install import check_registry

console = Console()

def check_command(cmd):
    try:
        # On windows we use shell=True or the specific executable name
        subprocess.run(f"{cmd} --version", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        return True
    except Exception:
        return False

def check_package_type(package):
    if package.startswith("http") or ("/" in package and not package.startswith("@")):
        return "direct"
    if check_registry(f"https://registry.npmjs.org/{package}"):
        return "npm"
    if check_registry(f"https://pypi.org/pypi/{package}/json"):
        return "pip"
    return None

def run_doctor(package):
    console.print("\n[bold cyan]🩺 Checking package...[/bold cyan]\n")
    time.sleep(1)
    
    # Check Network
    network = False
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        requests.get("https://github.com", headers=headers, timeout=10)
        network = True
    except:
        pass

    # Check Storage
    total, used, free = shutil.disk_usage("/")
    storage = free > (50 * 1024 * 1024) # 50 MB free
    
    # Check Package & Dependencies
    pkg_type = check_package_type(package)
    deps = False
    if pkg_type == "npm":
        deps = check_command("npm")
    elif pkg_type == "pip":
        deps = check_command("pip")
    elif pkg_type == "direct":
        deps = True
        
    # Output
    if deps:
        console.print("[green]✅ Dependencies installed[/green]")
    else:
        if pkg_type == "npm":
            console.print("[red]❌ NPM is not installed[/red]")
        elif pkg_type == "pip":
            console.print("[red]❌ PIP is not installed[/red]")
        else:
            console.print("[red]❌ Package not found, cannot check dependencies[/red]")
            
    if network:
        console.print("[green]✅ Network available[/green]")
    else:
        console.print("[red]❌ Network unavailable[/red]")
        
    if storage:
        console.print("[green]✅ Storage available[/green]")
    else:
        console.print("[red]❌ Insufficient storage[/red]")
        
    console.print("\n[bold]Diagnosis:[/bold]")
    if pkg_type and deps and network and storage:
        console.print("[green]Ready for installation.[/green]\n")
    elif not pkg_type:
        console.print("[red]Package not found on NPM, PyPI, or GitHub.[/red]\n")
    else:
        console.print("[yellow]System not ready for installation. Fix the issues above.[/yellow]\n")
