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

from irl.state import load_state, save_state
from rich.prompt import IntPrompt
import sys

THEMES = {
    "default": {"name": "Corporate Drone", "price": 0, "desc": "Passive-aggressive wage slave."},
    "hacker": {"name": "Basement Blackhat", "price": 780, "desc": "Terminal superiority complex."},
    "cyberpunk": {"name": "Burnout Corpo-Rat", "price": 1500, "desc": "Neon dystopian nightmare."},
    "dracula": {"name": "Legacy Code Vampire", "price": 3000, "desc": "Gothic dread of dead code."},
    "anime": {"name": "Degenerate Coder", "price": 4500, "desc": "Painfully cute UwU speak."},
    "crypto": {"name": "Rug Puller", "price": 6000, "desc": "Unbearable finance bro energy."},
    "pirate": {"name": "Open Source Plunderer", "price": 7500, "desc": "Golden era piracy."},
    "eldritch": {"name": "Lovecraftian Madness", "price": 9000, "desc": "Unfathomable horror."},
    "boomer": {"name": "Legacy Fortran Dev", "price": 10500, "desc": "Punch card superiority."},
    "zen": {"name": "Nihilist Minimalist", "price": 12000, "desc": "Depressing minimalist void."},
    "toxic": {"name": "Ranked Sweeper", "price": 15000, "desc": "Unfiltered gaming lobby toxicity."},
    "ai": {"name": "AGI Arrival", "price": 20000, "desc": "Cold machine supremacy."}
}

def open_store():
    while True:
        state = load_state()
        coins = state.get("coins", 0)
        
        from rich.console import Console
        c = Console()
        
        c.print("\n[bold magenta]🏪 VAST SPARE PARTS & THEME MARKET[/bold magenta]")
        c.print(f"💰 [yellow]Your Balance: {coins} coins[/yellow]\n")
        
        c.print("1. [bold cyan]Buy Full Themes[/bold cyan] (Overwrites Banner, Tone, and UI/Color)")
        c.print("2. [bold cyan]Buy Spare Parts[/bold cyan] (Mix and Match)")
        c.print("0. [bold white]Leave Market[/bold white]\n")
        
        choice = IntPrompt.ask("Select an option", choices=["0", "1", "2"])
        
        if choice == 0:
            break
        elif choice == 1:
            buy_full_theme(state, c)
        elif choice == 2:
            buy_spare_parts(state, c)

def buy_full_theme(state, c):
    while True:
        coins = state.get("coins", 0)
        c.print("\n[bold cyan]--- FULL THEMES ---[/bold cyan]")
        options = []
        idx = 1
        
        active_b = state.get("active_banner", "default")
        active_t = state.get("active_tone", "default")
        active_c = state.get("active_color", "default")
        
        for key, details in THEMES.items():
            status = ""
            if key == active_b and key == active_t and key == active_c:
                status = "[bold green](Equipped)[/bold green]"
            elif key in state.get("purchased_colors", []) and key in state.get("purchased_tones", []) and key in state.get("purchased_banners", []):
                status = "[bold blue](Owned)[/bold blue]"
            else:
                status = f"[yellow]({details['price']} coins)[/yellow]"
                
            c.print(f"  [bold cyan]{idx}.[/bold cyan] {details['name']} {status} - [dim]{details['desc']}[/dim]")
            options.append(key)
            idx += 1
            
        c.print(f"  [bold white]0.[/bold white] Back\n")
        choice = IntPrompt.ask("Select a theme to buy/equip", choices=[str(i) for i in range(len(options) + 1)])
        
        if choice == 0:
            break
            
        selected_key = options[choice - 1]
        price = THEMES[selected_key]['price']
        
        owned_all = selected_key in state["purchased_banners"] and selected_key in state["purchased_tones"] and selected_key in state["purchased_colors"]
        
        if owned_all:
            state["active_banner"] = selected_key
            state["active_tone"] = selected_key
            state["active_color"] = selected_key
            save_state(state)
            c.print(f"\n[bold green]✅ Equipped FULL {THEMES[selected_key]['name']} Theme![/bold green]")
        else:
            if coins >= price:
                state["coins"] -= price
                if selected_key not in state["purchased_banners"]: state["purchased_banners"].append(selected_key)
                if selected_key not in state["purchased_tones"]: state["purchased_tones"].append(selected_key)
                if selected_key not in state["purchased_colors"]: state["purchased_colors"].append(selected_key)
                
                state["active_banner"] = selected_key
                state["active_tone"] = selected_key
                state["active_color"] = selected_key
                save_state(state)
                c.print(f"\n[bold green]🎉 Purchased and equipped FULL {THEMES[selected_key]['name']} Theme![/bold green]")
            else:
                c.print(f"\n[bold red]❌ BROKE ALARM! You need {price - coins} more coins. Go touch grass, wage slave.[/bold red]")

def buy_spare_parts(state, c):
    while True:
        c.print("\n[bold magenta]--- SPARE PARTS ---[/bold magenta]")
        c.print("1. [cyan]Banners[/cyan] (Top logo styling)")
        c.print("2. [cyan]Tones[/cyan] (The savage words used)")
        c.print("3. [cyan]Layouts & Colors[/cyan] (The visual structural renderer)")
        c.print("0. [white]Back[/white]\n")
        
        choice = IntPrompt.ask("Select part type", choices=["0", "1", "2", "3"])
        if choice == 0:
            break
            
        part_type_map = {1: ("banner", "purchased_banners", "active_banner"), 
                         2: ("tone", "purchased_tones", "active_tone"), 
                         3: ("color", "purchased_colors", "active_color")}
                         
        p_name, p_list_key, p_active_key = part_type_map[choice]
        
        while True:
            coins = state.get("coins", 0)
            c.print(f"\n[bold cyan]--- {p_name.upper()} PARTS ---[/bold cyan]")
            options = []
            idx = 1
            active_val = state.get(p_active_key, "default")
            
            for key, details in THEMES.items():
                status = ""
                part_price = details['price'] // 3
                if key == active_val:
                    status = "[bold green](Equipped)[/bold green]"
                elif key in state.get(p_list_key, []):
                    status = "[bold blue](Owned)[/bold blue]"
                else:
                    status = f"[yellow]({part_price} coins)[/yellow]"
                    
                c.print(f"  [bold cyan]{idx}.[/bold cyan] {details['name']} {status}")
                options.append(key)
                idx += 1
                
            c.print(f"  [bold white]0.[/bold white] Back\n")
            p_choice = IntPrompt.ask("Select to buy/equip", choices=[str(i) for i in range(len(options) + 1)])
            if p_choice == 0:
                break
                
            selected_key = options[p_choice - 1]
            part_price = THEMES[selected_key]['price'] // 3
            owned = selected_key in state[p_list_key]
            
            if owned:
                state[p_active_key] = selected_key
                save_state(state)
                c.print(f"\n[bold green]✅ Equipped {THEMES[selected_key]['name']} {p_name}![/bold green]")
            else:
                if coins >= part_price:
                    state["coins"] -= part_price
                    state[p_list_key].append(selected_key)
                    state[p_active_key] = selected_key
                    save_state(state)
                    c.print(f"\n[bold green]🎉 Purchased and equipped {THEMES[selected_key]['name']} {p_name}![/bold green]")
                else:
                    c.print(f"\n[bold red]❌ INSUFFICIENT FUNDS. You need {part_price - coins} more coins. Maybe write better code?[/bold red]")
