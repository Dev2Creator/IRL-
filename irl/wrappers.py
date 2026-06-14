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

import subprocess
import sys
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn

def run_with_progress(command_str, package, manager_name):
    print(f"\nPreparing to install {package} using {manager_name}...")
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task(f"[green]🌱 Touching grass... Installing {package}...", start=False)
        
        process = subprocess.Popen(
            command_str,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )
        
        stdout, stderr = process.communicate()
        
    if process.returncode == 0:
        print(f"✨ Successfully touched grass and installed the package!")
        return True
    else:
        print(f"❌ Failed to install {package}.")
        if stderr:
            print(stderr.decode("utf-8", errors="ignore"))
        return False

def install_npm(package):
    return run_with_progress(f"npm install {package}", package, "npm")

def install_pip(package):
    return run_with_progress(f"pip install {package}", package, "pip")
