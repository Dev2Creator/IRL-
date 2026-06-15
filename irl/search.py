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
    console.print(f"\n[bold cyan]IRL AI™[/bold cyan] is searching the knowledge banks for: [yellow]'{query}'[/yellow]...")
    
    prompt = f"What is the most popular Python pip package for: {query}? Reply with ONLY the exact pip package name and absolutely nothing else. No explanation, no markdown formatting, no quotes, just the name."
    url = "https://text.pollinations.ai/" + urllib.parse.quote(prompt)
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
        with urllib.request.urlopen(req, timeout=15) as response:
            result = response.read().decode('utf-8').strip()
            
        # Clean up the result just in case the AI added backticks or extra spaces
        result = result.replace("`", "").replace("'", "").replace('"', "").strip()
            
        if not result or len(result) > 50 or " " in result:
            console.print(f"[bold red]IRL AI™[/bold red] got confused and replied with: [dim]{result}[/dim]")
            console.print("[dim]Please try a more specific search.[/dim]")
            return
            
        console.print(f"\n✨ [bold green]IRL AI™ found the perfect package:[/bold green] [bold magenta]{result}[/bold magenta]")
        
        if Confirm.ask("\nWould you like to install it now?"):
            install_package(result)
            
    except Exception as e:
        console.print(f"[bold red]IRL AI™ Error:[/bold red] Could not connect to the hive mind. ({e})")
