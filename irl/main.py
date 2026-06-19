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
import os
import random
import shutil
import time
from rich import box
from rich.live import Live
from rich.layout import Layout
from rich.table import Table
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
    
    if os.path.isdir("node_modules"):
        engine.render_node_modules()
    
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
    city_parser = subparsers.add_parser("city", help="Enter the IRL City (Economy & Crime)")
    dashboard_parser = subparsers.add_parser("dashboard", help="Enter Chaotic Dashboard Mode")
    dash_parser = subparsers.add_parser("dash", help="Alias for Chaotic Dashboard Mode")
    manga_parser = subparsers.add_parser("manga", help="Read or Download IRL Manga")
    manga_parser.add_argument("--download", action="store_true", help="Download manga for offline reading")
    manga_parser.add_argument("query", nargs="*", help="Optional manga title search query")
    story_parser = subparsers.add_parser("story", help="Play the Themed Story Mode")
    bones_parser = subparsers.add_parser("bones", help="Summon Professor Bones for Lofi")
    joke_parser = subparsers.add_parser("joke", help="Tell a random developer joke via JokeAPI")
    dog_parser = subparsers.add_parser("dog", help="Fetch an ASCII dog from Dog API")
    search_parser = subparsers.add_parser("search", help="AI powered package search")
    search_parser.add_argument("query", nargs="+", help="Natural language query to find a package")
    upgrade_parser = subparsers.add_parser("upgrade", help="Upgrade IRL OS to the latest version")
    run_parser = subparsers.add_parser("run", help="Run a command wrapped in IRL OS (e.g. irl run dev)")
    run_parser.add_argument("cmd_args", nargs=argparse.REMAINDER, help="Command and arguments to run")
    
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
    elif args.command == "city":
        from irl.city import enter_city
        enter_city()
    elif args.command == "search":
        from irl.search import search_and_install
        search_and_install(" ".join(args.query))
    elif args.command == "upgrade":
        from irl.install import upgrade_irl
        upgrade_irl()
    elif args.command == "run":
        from irl.run import run_command
        if not args.cmd_args:
            print("Error: Please provide a command to run.")
            sys.exit(1)
        run_command(args.cmd_args)
    elif args.command == "manga":
        from irl.manga import read_manga
        query = " ".join(args.query) if args.query else None
        read_manga(download=args.download, initial_query=query)
    elif args.command == "story":
        from irl.story import play_story
        play_story()
    elif args.command == "bones":
        from irl.bones import summon_bones
        summon_bones()
    elif args.command == "joke":
        from irl.joke import tell_joke
        tell_joke()
    elif args.command == "dog":
        from irl.dog import render_dog
        render_dog()
    elif args.command in ("dashboard", "dash"):
        chaotic_dashboard_mode(loop=True)
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


CHAOS_TICKERS = [
    "node_modules detected: disk space has filed a restraining order.",
    "npm audit says everything is fine, which is how horror movies start.",
    "Your dependency tree has more unresolved trauma than the sprint retro.",
    "Localhost is running. So are your responsibilities.",
    "A package-lock changed. Nobody knows why. Everybody is pretending.",
    "Build succeeded with warnings: the compiler is legally distancing itself.",
    "Docker is eating 8GB RAM to serve one button. Premium suffering.",
    "The terminal saw your command history and quietly lowered its expectations.",
    "CI passed because it is tired of explaining things to you.",
    "A linter screamed. Management called it culture fit.",
]

CHAOS_TASKS = [
    ("Install a Package", "Summon third-party code and hope it showers."),
    ("Glasses", "Inspect a package before it inspects your soul."),
    ("Doctor", "Diagnose your dependency swamp."),
    ("Touch Grass", "Briefly cosplay as a mammal."),
    ("Creative Wellness", "Posture, water, denial, and other paid DLC."),
    ("IRL Store", "Buy personality presets. Cheaper than therapy."),
    ("Profile", "View quantified decay."),
    ("Games", "Productivity funeral minigames."),
    ("AI Search", "Ask the machine which package will betray you."),
    ("Upgrade IRL OS", "Download hope. Install consequences."),
    ("IRL City", "Economy, crime, and terminal capitalism."),
    ("IRL Manga", "Experience terminal degeneracy in Japanese formatting."),
    ("Story Mode", "Traverse a branching narrative of professional failure."),
    ("Summon Bones", "Lofi Beats to Compile Code To."),
    ("Tell Joke", "Fetch a Joke via JokeAPI."),
    ("Random Doggo", "Fetch an ASCII Dog via Dog API."),
]

DASHBOARD_MENU_CHOICES = [str(i) for i in range(len(CHAOS_TASKS) + 1)]


def _node_modules_report():
    path = os.path.join(os.getcwd(), "node_modules")
    if not os.path.isdir(path):
        return {
            "found": False,
            "path": path,
            "size": "0 MB",
            "files": 0,
            "roast": "No node_modules here. Suspiciously healthy. Are you lost?",
        }

    total_size = 0
    total_files = 0
    for root, _, files in os.walk(path):
        total_files += len(files)
        for name in files:
            try:
                total_size += os.path.getsize(os.path.join(root, name))
            except OSError:
                pass

    size_mb = total_size / (1024 * 1024)
    return {
        "found": True,
        "path": path,
        "size": f"{size_mb:,.1f} MB",
        "files": total_files,
        "roast": random.choice([
            "node_modules found. The landfill has become sentient.",
            "Your dependency folder qualifies as a minor geological event.",
            "That is not a folder. That is capitalism with subdirectories.",
            "Disk usage report: emotionally expensive.",
            "The package manager opened a buffet and charged your SSD.",
        ]),
    }


def _fake_stats(tick):
    width = shutil.get_terminal_size((100, 30)).columns
    return {
        "CPU Shame": f"{41 + ((tick * 7) % 59)}%",
        "RAM Regret": f"{33 + ((tick * 11) % 64)}%",
        "Bug Humidity": f"{55 + ((tick * 5) % 42)}%",
        "Stack Overflow Tabs": str(7 + ((tick * 3) % 81)),
        "Terminal Width": str(width),
        "Hope Remaining": f"{max(1, 23 - (tick % 23))}%",
    }


def _build_dashboard(state, rank, user_name, tick, selected=0):
    from irl.themes import get_engine
    from irl.themes.layouts import render_dashboard_chrome, DASHBOARD_SKINS

    engine = get_engine()
    skin = DASHBOARD_SKINS.get(engine.color_id, DASHBOARD_SKINS["default"])
    accent = skin["accent"]
    border = skin["border"]
    theme_box = skin["box"]

    node = _node_modules_report()
    stats = _fake_stats(tick)
    ticker_offset = tick % len(CHAOS_TICKERS)
    ticker = "  //  ".join(CHAOS_TICKERS[ticker_offset:] + CHAOS_TICKERS[:ticker_offset])

    menu = Table.grid(expand=True)
    menu.add_column(ratio=1)
    for idx, (label, desc) in enumerate(CHAOS_TASKS, start=1):
        if idx - 1 == selected:
            style = f"bold black on {accent}"
            cursor = ">"
        else:
            style = f"bold {border}"
            cursor = " "
        menu.add_row(f"[{style}] {cursor} {idx:02}. {label}[/]")
        menu.add_row(f"[dim]     {desc}[/dim]")
        
    menu.add_row("")
    menu.add_row(f"[{accent}]CONTROLS: \[W]/\[S] or \[UP]/\[DOWN] to scroll • \[ENTER] to select • \[Q] to exit[/{accent}]")

    stats_table = Table(show_header=False, box=theme_box, expand=True)
    stats_table.add_column("Metric", style=f"bold {border}")
    stats_table.add_column("Value", justify="right", style=f"bold {accent}")
    for key, value in stats.items():
        stats_table.add_row(key, value)

    node_table = Table(show_header=False, box=theme_box, expand=True)
    node_table.add_column("K", style=f"bold {border}")
    node_table.add_column("V", style="white", overflow="fold")
    node_table.add_row("Found", "YES, unfortunately" if node["found"] else "No")
    node_table.add_row("Path", node["path"])
    node_table.add_row("Size", node["size"])
    node_table.add_row("Files", str(node["files"]))

    layout = Layout()
    layout.split_column(
        Layout(name="header", size=6),
        Layout(name="main", ratio=1, minimum_size=13),
        Layout(name="ticker", size=3),
    )
    layout["main"].split_row(
        Layout(name="left", ratio=2, minimum_size=38),
        Layout(name="right", ratio=1, minimum_size=30),
    )
    layout["right"].split_column(
        Layout(name="stats"),
        Layout(name="node"),
    )

    layout["header"].update(render_dashboard_chrome("header", engine.color_id, user_name, rank, tick))
    layout["left"].update(render_dashboard_chrome("menu", engine.color_id, menu, selected, tick))
    layout["stats"].update(render_dashboard_chrome("stats", engine.color_id, stats_table, None, tick))
    layout["node"].update(render_dashboard_chrome("node", engine.color_id, node_table, node["roast"], tick))
    
    # Use theme colors for the ticker
    ticker_text = f"[bold {border}]DARK HUMOR INCIDENT FEED[/bold {border}]"
    layout["ticker"].update(render_dashboard_chrome("ticker", engine.color_id, ticker, ticker_text, tick))
    return layout


def _dispatch_dashboard_choice(choice):
    from rich.prompt import Prompt

    if choice == 0:
        return False
    if choice == 1:
        pkg = Prompt.ask("Package name or URL")
        if pkg:
            install_package(pkg)
    elif choice == 2:
        pkg = Prompt.ask("Package to inspect")
        if pkg:
            inspect_package(pkg)
    elif choice == 3:
        pkg = Prompt.ask("Package to diagnose")
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
        query = Prompt.ask("What package are you looking for?")
        if query:
            from irl.search import search_and_install
            search_and_install(query)
    elif choice == 10:
        from irl.install import upgrade_irl
        upgrade_irl()
    elif choice == 11:
        from irl.city import enter_city
        enter_city()
    elif choice == 12:
        from irl.manga import read_manga
        read_manga()
    elif choice == 13:
        from irl.story import play_story
        play_story()
    elif choice == 14:
        from irl.bones import summon_bones
        summon_bones()
    elif choice == 15:
        from irl.joke import tell_joke
        tell_joke()
    elif choice == 16:
        from irl.dog import render_dog
        render_dog()
    return True


def chaotic_dashboard_mode(loop=False):
    from irl.console import console
    from irl.state import load_state, get_global_rank
    import msvcrt

    while True:
        state = load_state()
        user_name = state.get("name", "human")
        rank = get_global_rank(state)
        selected = 0
        
        # ROBUST FLUSH: Terminals can take a split second to send the Enter key
        # that was used to launch the command. We must wait and flush completely.
        end_flush = time.time() + 0.35
        while time.time() < end_flush:
            while msvcrt.kbhit():
                msvcrt.getch()
            time.sleep(0.01)
        
        # Open the full-screen alternate buffer
        with console._console.screen():
            # Animate infinitely, tracking keypresses
            with Live(
                _build_dashboard(state, rank, user_name, 0, selected),
                console=console._console,
                screen=False,
                refresh_per_second=10,
            ) as live:
                tick = 0
                chosen = None
                
                while True:
                    live.update(_build_dashboard(state, rank, user_name, tick, selected))
                    time.sleep(0.1) # 10 FPS animation
                    tick += 1
                    
                    while msvcrt.kbhit():
                        key = msvcrt.getch()
                        if key in (b'\xe0', b'\x00'): # Arrow keys
                            arrow = msvcrt.getch()
                            if arrow == b'H': # Up
                                selected = (selected - 1) % len(CHAOS_TASKS)
                            elif arrow == b'P': # Down
                                selected = (selected + 1) % len(CHAOS_TASKS)
                        else:
                            key_lower = key.lower()
                            if key_lower == b'w':
                                selected = (selected - 1) % len(CHAOS_TASKS)
                            elif key_lower == b's':
                                selected = (selected + 1) % len(CHAOS_TASKS)
                            elif key in (b'\r', b'\n', b' '):
                                chosen = selected + 1
                                break
                            elif key_lower in (b'q', b'\x1b') or key == b'0':
                                chosen = 0
                                break
                                
                    if chosen is not None:
                        break

        if chosen == 0:
            break
        
        keep_going = _dispatch_dashboard_choice(chosen)
        if not loop or not keep_going:
            break

def interactive_menu():
    chaotic_dashboard_mode(loop=True)

if __name__ == "__main__":
    cli()
