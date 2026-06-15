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

import urllib.request
import urllib.parse
import sys
from rich.prompt import Confirm
from irl.console import console
from irl.install import install_package

def search_and_install(query: str):
    import re
    import time
    console.print(f"\n[bold cyan]IRL AI™[/bold cyan] is searching the knowledge banks for: [yellow]'{query}'[/yellow]...")
    
    prompt = f"What is the Python pip package for: {query}? Reply with exactly one word: the pip package name. No markdown, no quotes, no explanation."
    url = "https://text.pollinations.ai/" + urllib.parse.quote(prompt)
    
    result = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) IRL-OS/1.0'})
            with urllib.request.urlopen(req, timeout=15) as response:
                raw_result = response.read().decode('utf-8').strip()
            
            # Extract anything between backticks if they exist
            match = re.search(r'`([^`]+)`', raw_result)
            if match:
                result = match.group(1).strip()
            else:
                # Clean up any surrounding spaces or quotes
                result = raw_result.replace("'", "").replace('"', "").strip()
                # If there are spaces, take the last word (often "The package is requests" -> "requests")
                if " " in result:
                    result = result.split()[-1].strip('.')
            
            if result and len(result) < 50 and " " not in result:
                break # Good result
            else:
                result = None
                time.sleep(1) # Try again
                
        except Exception as e:
            if attempt == 2:
                console.print(f"[bold red]IRL AI™ Error:[/bold red] Could not connect to the hive mind. ({e})")
                return
            time.sleep(1)
            
    if not result:
        console.print(f"[bold red]IRL AI™[/bold red] got confused and replied with garbage.")
        console.print("[dim]Please try a more specific search.[/dim]")
        return
        
    console.print(f"\n✨ [bold green]IRL AI™ found the perfect package:[/bold green] [bold magenta]{result}[/bold magenta]")
    
    if Confirm.ask("\nWould you like to install it now?"):
        install_package(result)
