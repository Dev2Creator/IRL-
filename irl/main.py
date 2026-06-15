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

import argparse
import sys
from irl.install import install_package
from irl.glasses import inspect_package
from irl.doctor import run_doctor

def cli():
    from irl.state import load_state, save_state
    from irl.console import console
    from rich.prompt import Prompt
    
    state = load_state()
    if not state.get("name"):
        console.print("\n[bold cyan]IRL™ OS Initialization...[/bold cyan]")
        user_name = Prompt.ask("What is your name, organic lifeform?")
        state["name"] = user_name
        save_state(state)

    from irl.themes import get_engine
    engine = get_engine()
    engine.render_banner()
    
    parser = argparse.ArgumentParser(
        prog="irl",
        description="IRL™ (In Real Life™) - Software for Humans™."
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    install_parser = subparsers.add_parser("install", help="Get Started")
    install_parser.add_argument("package", help="Name of the package, GitHub repo, or direct URL")
    
    glasses_parser = subparsers.add_parser("glasses", help="See Clearly")
    glasses_parser.add_argument("package", help="Name of the package to inspect")
    
    doctor_parser = subparsers.add_parser("doctor", help="Stay Healthy")
    doctor_parser.add_argument("package", help="Name of the package to diagnose")
    
    grass_parser = subparsers.add_parser("grass", help="Go Outside")
    posture_parser = subparsers.add_parser("posture", help="Fix your posture")
    window_parser = subparsers.add_parser("window", help="Look outside")
    mirror_parser = subparsers.add_parser("mirror", help="Get a compliment")
    hydrate_parser = subparsers.add_parser("hydrate", help="Drink water")
    chaos_parser = subparsers.add_parser("chaos", help="Take the chaos quiz")
    store_parser = subparsers.add_parser("store", help="Open the IRL store")
    games_parser = subparsers.add_parser("games", help="Play purchased IRL games")
    search_parser = subparsers.add_parser("search", help="AI powered package search")
    search_parser.add_argument("query", nargs="+", help="Natural language query to find a package")
    upgrade_parser = subparsers.add_parser("upgrade", help="Upgrade IRL OS to the latest version")
    
    args = parser.parse_args()
    
    from datetime import datetime
    current_hour = datetime.now().hour
    if 1 <= current_hour <= 4:
        engine.ui.render_generic("⚠️ It's late. The bugs will still be there tomorrow. Go to sleep.")
    
    if args.command == "install":
        if not args.package:
            print("Error: Please provide a package name to install.")
            sys.exit(1)
        install_package(args.package)
    elif args.command == "glasses":
        if not args.package:
            print("Error: Please provide a package name to inspect.")
            sys.exit(1)
        inspect_package(args.package)
    elif args.command == "doctor":
        if not args.package:
            print("Error: Please provide a package name to diagnose.")
            sys.exit(1)
        run_doctor(args.package)
    elif args.command == "grass":
        from irl.grass import touch_grass
        touch_grass()
    elif args.command == "posture":
        from irl.creative import posture
        posture()
    elif args.command == "window":
        from irl.creative import window
        window()
    elif args.command == "mirror":
        from irl.creative import mirror
        mirror()
    elif args.command == "hydrate":
        from irl.creative import hydrate
        hydrate()
    elif args.command == "chaos":
        from irl.creative import chaos
        chaos()
    elif args.command == "store":
        from irl.store import open_store
        open_store()
    elif args.command == "games":
        from irl.games import play_game_menu
        play_game_menu()
    elif args.command == "search":
        from irl.search import search_and_install
        search_and_install(" ".join(args.query))
    elif args.command == "upgrade":
        from irl.install import upgrade_irl
        upgrade_irl()
    else:
        interactive_menu()

def creative_menu():
    from rich.prompt import IntPrompt
    from rich.console import Console
    console = Console()
    
    while True:
        console.print("\n[bold magenta]🎨 Creative Wellness Menu™[/bold magenta]")
        console.print("  [bold magenta]1.[/bold magenta] 🦐 Fix your posture™")
        console.print("  [bold blue]2.[/bold blue] 💧 Hydrate™")
        console.print("  [bold cyan]3.[/bold cyan] 🪟 Look outside™")
        console.print("  [bold magenta]4.[/bold magenta] 🪞 Get a compliment™")
        console.print("  [bold yellow]5.[/bold yellow] 🌪️  Chaos Quiz™")
        console.print("  [bold green]6.[/bold green] 🎭 Chaos Counter™ (Daily Joke™)")
        console.print("  [bold white]0.[/bold white] Back to Main Menu™\n")
        
        choice = IntPrompt.ask("Select an option", choices=["0", "1", "2", "3", "4", "5", "6"], console=console)
        
        if choice == 0:
            break
        elif choice == 1:
            from irl.creative import posture
            posture()
        elif choice == 2:
            from irl.creative import hydrate
            hydrate()
        elif choice == 3:
            from irl.creative import window
            window()
        elif choice == 4:
            from irl.creative import mirror
            mirror()
        elif choice == 5:
            from irl.creative import chaos
            chaos()
        elif choice == 6:
            from irl.creative import chaos_counter
            chaos_counter()

def view_profile():
    from irl.state import load_state, get_global_rank
    from irl.console import console
    from rich.panel import Panel
    from rich.table import Table
    import os, json

    state = load_state()
    user_name = state.get("name", "Unknown")
    rank = get_global_rank(state)
    
    table = Table(show_header=False, box=None)
    table.add_column("Stat", style="bold cyan")
    table.add_column("Value", style="bold yellow")
    
    table.add_row("Rank", rank)
    table.add_row("Total XP", str(state.get("total_xp", 0)))
    table.add_row("Coins", str(state.get("coins", 0)))
    table.add_row("Active Banner", state.get("active_banner", "default").title())
    table.add_row("Active Tone", state.get("active_tone", "default").title())
    table.add_row("Active Layout", state.get("active_color", "default").title())
    
    # Try to get grass stats
    grass_file = os.path.expanduser("~/.irl_grass.json")
    if os.path.exists(grass_file):
        try:
            with open(grass_file, 'r') as f:
                g_state = json.load(f)
                table.add_row("Grass Streak", str(g_state.get("streak", 0)))
        except: pass

    panel = Panel(table, title=f"[bold magenta]👤 {user_name}'s IRL™ Profile[/bold magenta]", border_style="cyan")
    console.print(panel)
    
    from rich.prompt import Prompt
    Prompt.ask("\nPress Enter to return")

def interactive_menu():
    from rich.prompt import Prompt, IntPrompt
    from rich.console import Console
    console = Console()
    
    from irl.state import load_state, get_global_rank
    state = load_state()
    user_name = state.get("name", "human")
    rank = get_global_rank(state)
    
    while True:
        console.print(f"\n[bold cyan]What would you like to do, [{rank}] {user_name}?[/bold cyan]")
        console.print("  [bold yellow]1.[/bold yellow] 📦 Install a Package™")
        console.print("  [bold cyan]2.[/bold cyan] 👓 Inspect a Package (Glasses™)")
        console.print("  [bold red]3.[/bold red] 🩺 Diagnose System (Doctor™)")
        console.print("  [bold green]4.[/bold green] 🌱 Touch Grass™")
        console.print("  [bold magenta]5.[/bold magenta] 🎨 Creative Wellness Menu™")
        console.print("  [bold yellow]6.[/bold yellow] 🏪 Open IRL™ Store")
        console.print("  [bold blue]7.[/bold blue] 📊 View IRL™ Profile & Stats")
        console.print("  [bold cyan]8.[/bold cyan] 🎮 Play Games™")
        console.print("  [bold magenta]9.[/bold magenta] 🧠 AI Package Search™ (Pollination AI)")
        console.print("  [bold green]10.[/bold green] 🚀 Upgrade IRL™ OS")
        console.print("  [bold white]0.[/bold white] Exit\n")
        
        choice = IntPrompt.ask("Select an option", choices=[str(i) for i in range(11)], console=console)
        
        if choice == 0:
            console.print("[dim]Goodbye, human.[/dim]")
            sys.exit(0)
        elif choice == 1:
            pkg = Prompt.ask("Enter package name or URL")
            if pkg:
                install_package(pkg)
        elif choice == 2:
            pkg = Prompt.ask("Enter package name to inspect")
            if pkg:
                inspect_package(pkg)
        elif choice == 3:
            pkg = Prompt.ask("Enter package name to diagnose")
            if pkg:
                run_doctor(pkg)
        elif choice == 4:
            from irl.grass import touch_grass
            touch_grass()
        elif choice == 5:
            creative_menu()
        elif choice == 6:
            from irl.store import open_store
            open_store()
        elif choice == 7:
            view_profile()
        elif choice == 8:
            from irl.games import play_game_menu
            play_game_menu()
        elif choice == 9:
            query = Prompt.ask("What kind of package are you looking for?")
            if query:
                from irl.search import search_and_install
                search_and_install(query)
        elif choice == 10:
            from irl.install import upgrade_irl
            upgrade_irl()

if __name__ == "__main__":
    cli()
