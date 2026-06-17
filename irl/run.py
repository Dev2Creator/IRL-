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

import os
import subprocess
from irl.themes import get_engine

def run_command(cmd_args):
    engine = get_engine()
    
    use_npm = False
    if os.path.exists("package.json"):
        use_npm = True
    
    cmd_str = " ".join(cmd_args)
    if use_npm:
        full_cmd = ["npm", "run"] + cmd_args
        display_cmd = f"npm run {cmd_str}"
    else:
        full_cmd = cmd_args
        display_cmd = cmd_str
        
    engine.render_run_start(display_cmd)
    
    try:
        # Pass through the process directly to terminal
        subprocess.run(full_cmd, shell=True, check=True)
        engine.render_run_success(display_cmd)
    except subprocess.CalledProcessError as e:
        engine.ui.render_generic(f"[bold red]❌ Command failed with code {e.returncode}[/bold red]")
    except Exception as e:
        engine.ui.render_generic(f"[bold red]❌ Failed to run command: {e}[/bold red]")
