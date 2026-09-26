# IRL™ 🌱 - Software for Humans
# Copyright (C) 2026 Anika Mukherjee
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
import json
import os
import random
import shutil
import sys
import time

from rich import box
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table

from irl.doctor import run_doctor
from irl.glasses import inspect_package
from irl.install import install_package
from irl.rollback import rollback_irl

IRL_ACCENT = "#F29265"
IRL_CREAM = "#D7C0AA"
IRL_MUTED = "#614B39"
IRL_BORDER = "#6B4E36"
IRL_SELECT = "#3478F6"

IRL_COMMANDS = [
    ("install", "Install a package, repo, or URL", "install"),
    ("glasses", "Inspect a package before trusting it", "glasses"),
    ("doctor", "Diagnose a package like a calm terminal medic", "doctor"),
    ("grass", "Touch grass; outdoor patch installed", "grass"),
    ("posture", "Fix your posture before the stone judges you", "posture"),
    ("hydrate", "Drink water; bugs hate hydration", "hydrate"),
    ("search", "Find a useful package with AI help", "search"),
    ("store", "Open the IRL store", "store"),
    ("games", "Play purchased IRL games", "games"),
    ("dashboard", "Enter the full terminal command board", "dashboard"),
    ("city", "Enter IRL City economy mode", "city"),
    ("manga", "Read or download IRL Manga", "manga"),
    ("story", "Play the themed story mode", "story"),
    ("bones", "Summon Professor Bones for lofi", "bones"),
    ("joke", "Fetch a developer joke", "joke"),
    ("dog", "Summon an ASCII dog", "dog"),
    ("upgrade", "Upgrade IRL OS", "upgrade"),
    ("rollback", "Roll back to an older IRL version", "rollback"),
    ("pet", "Visit your terminal pet", "pet"),
    ("quests", "See today's daily quests", "quests"),
    ("achievements", "View trophies and your dev level", "achievements"),
    ("grassland", "Play Grassland Quest (free roguelike)", "grassland"),
    ("rhythm", "Play Lofi Rhythm (beat game)", "rhythm"),
    ("lang", "Run the .irl toy language", "lang"),
    ("tui", "Launch the full-screen TUI (needs irl-pkg[tui])", "tui"),
    ("exit", "Leave IRL", "exit"),
]


def _get_identity_line(state):
    try:
        import json
        from pathlib import Path

        profile_path = Path.home() / ".irl" / "profile.json"
        if profile_path.exists():
            profile = json.loads(profile_path.read_text(encoding="utf-8"))
            name = profile.get("name") or state.get("name")
            pronouns = profile.get("pronouns")
            pronunciation = profile.get("name_pronunciation")
            if name:
                pronunciation_text = f" [{IRL_MUTED}]({pronunciation})[/{IRL_MUTED}]" if pronunciation else ""
                pronouns_text = f" [{IRL_CREAM}]• {pronouns}[/{IRL_CREAM}]" if pronouns else ""
                return f"[{IRL_MUTED}]Identity   [/{IRL_MUTED}][{IRL_ACCENT}]🗿 {name}[/{IRL_ACCENT}]{pronunciation_text}{pronouns_text}\n"
    except Exception:
        pass
    name = state.get("name") or "traveler"
    return f"[{IRL_MUTED}]Identity   [/{IRL_MUTED}][{IRL_ACCENT}]🗿 {name}[/{IRL_ACCENT}]\n"


def _print_irl_wisdom_header(state=None):
    from datetime import datetime

    from rich import box
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text

    c = Console(highlight=False)
    state = state or {}
    title = Text("IRL", style=f"bold {IRL_ACCENT}")
    title.append("\nWISDOM OS", style=f"bold {IRL_ACCENT}")
    c.print(title)
    c.print(Text("✦  Software for humans. Terminal rituals. Useful choices.  ✦", style=IRL_CREAM))
    c.print()

    status_text = (
        _get_identity_line(state)
        + f"[{IRL_MUTED}]Mode       [/{IRL_MUTED}][{IRL_CREAM}]Ready[/{IRL_CREAM}]\n"
        + f"[{IRL_MUTED}]Today      [/{IRL_MUTED}][{IRL_CREAM}]{datetime.now().strftime('%Y-%m-%d')}[/{IRL_CREAM}]\n"
        + f"[{IRL_MUTED}]Stone      [/{IRL_MUTED}][{IRL_ACCENT}]The useful command remembers you.[/{IRL_ACCENT}]"
    )
    c.print(Panel(status_text, border_style=IRL_BORDER, box=box.SQUARE, expand=True, width=min(88, max(52, c.width - 2)), padding=(0, 1)))

    line = Text()
    line.append("● ", style=IRL_ACCENT)
    line.append("irl       ", style=IRL_MUTED)
    line.append("Ready — choose a command below", style=IRL_CREAM)
    c.print(line)
    version_line = Text("IRL™ ", style=IRL_MUTED)
    version_line.append("terminal-safe human software", style=f"bold {IRL_ACCENT}")
    c.print(version_line)
    c.print()
    return c


def _render_irl_custom_help(state=None):
    from rich.table import Table

    c = _print_irl_wisdom_header(state or {})
    table = Table(show_header=False, box=None, expand=True, pad_edge=False)
    table.add_column("Command", style=f"bold {IRL_ACCENT}", no_wrap=True)
    table.add_column("Description", style=IRL_CREAM)
    for command, description, _ in IRL_COMMANDS:
        if command == "exit":
            continue
        table.add_row(f"/{command:<11}", description)
    c.print(table)
    c.print()
    c.print(f"[{IRL_MUTED}](Use `irl <command> --help` for command-specific options.)[/{IRL_MUTED}]")


def _run_shared_identity_first_run():
    try:
        from irl_identity.first_run import ensure_first_run_login

        ensure_first_run_login("irl", app_label="IRL", argv=sys.argv)
    except Exception:
        return


def _sync_shared_identity_name(state):
    try:
        from irl_identity.profile import load_profile

        profile = load_profile() or {}
        name = profile.get("name")
        if name and not state.get("name"):
            state["name"] = name
            return True
    except Exception:
        return False
    return False


IRL_VERSION = "2.0.0"


def unlock_matrix_theme():
    """Secret unlock: adds the Matrix theme to the state, free of charge."""
    from irl.state import load_state, save_state

    state = load_state()
    unlocked = state.setdefault("unlocked_themes", [])
    if "matrix" not in unlocked:
        unlocked.append("matrix")
        for part in ("purchased_banners", "purchased_tones", "purchased_colors"):
            if "matrix" not in state.setdefault(part, []):
                state[part].append("matrix")
        save_state(state)
        return True
    return False


def _run_onboarding(state):
    """Animated first-run ritual: splash, name, theme, and a very short tour."""
    import time as _time

    from rich.console import Console
    from rich.live import Live
    from rich.prompt import IntPrompt, Prompt

    from irl.ui import IRL_CREAM, IRL_MUTED, wordmark

    c = Console(highlight=False)
    from irl.state import save_state

    # --- Splash ---
    frames = ["🌱", "🌱🌱", "🌿🌱🌱", "🌿🌿🌱🌱", "🌿🌿🌿🌱", "🌿🌿🌿🌿"]
    try:
        with Live(console=c, refresh_per_second=8) as live:
            for frame in frames:
                live.update(wordmark(subtitle=f"{frame} planting your terminal garden... {frame}"))
                _time.sleep(0.22)
            live.update(wordmark())
    except Exception:
        c.print(wordmark())

    if not state.get("name"):
        name = Prompt.ask(f"[{IRL_CREAM}]What is your name, organic lifeform?[/{IRL_CREAM}]").strip()
        state["name"] = name or "human"

    # --- Theme picker (live previews of a few flavors) ---
    from irl.themes.layouts import DASHBOARD_SKINS

    choices = ["default", "hacker", "synthwave", "sakura", "termclassic", "highcontrast"]
    c.print(f"\n[{IRL_MUTED}]Pick a starting vibe. You can buy more in the store later:[/{IRL_MUTED}]\n")
    for idx, theme_id in enumerate(choices, start=1):
        c.print(f"  [bold]{idx}.[/bold] {DASHBOARD_SKINS[theme_id]['title']}")
    picked = IntPrompt.ask("Vibe number", default=1)
    picked_id = choices[picked - 1] if 1 <= picked <= len(choices) else "default"
    for part in ("active_banner", "active_tone", "active_color"):
        state[part] = picked_id
    for part in ("purchased_banners", "purchased_tones", "purchased_colors"):
        if picked_id not in state.setdefault(part, []):
            state[part].append(picked_id)
    state["onboarded_v2"] = True
    save_state(state)

    from irl.ui import preview_theme

    preview_theme(picked_id, console=c)
    c.print(f"[{IRL_CREAM}]Welcome aboard, {state['name']}. The 30-second tour:[/{IRL_CREAM}]")
    tour = [
        "1. `irl install requests` installs from PyPI, npm, GitHub or a URL. It just knows.",
        "2. `irl dashboard` is your mission control (arrow keys + Enter, Q to leave).",
        "3. `irl grass` touches grass. Daily. There is a streak. You will protect it.",
        "4. `irl games` hides a garden roguelike and a rhythm game. Coins are earned there.",
        "5. Something in this terminal is locked. Codes open doors. That is all we say.",
    ]
    for line in tour:
        c.print(f"[{IRL_MUTED}]{line}[/{IRL_MUTED}]")
        _time.sleep(1.6)
    c.print(f"\n[bold {IRL_ACCENT}]Tour complete. Zero dollars charged for the personality.[/bold {IRL_ACCENT}]")


def cli():
    """Entry point with beautiful failures: no raw tracebacks for humans."""
    from irl.console import console

    try:
        _cli_impl()
    except KeyboardInterrupt:
        console.print(f"\n[{IRL_MUTED}]Interrupted. The grass will wait.[/{IRL_MUTED}]")
        raise SystemExit(130) from None
    except EOFError:
        console.print(f"\n[{IRL_MUTED}]No input found. IRL runs on humans; connect one and retry.[/{IRL_MUTED}]")
        raise SystemExit(1) from None
    except Exception as exc:
        from irl.ui import styled_error

        if os.environ.get("IRL_DEBUG"):
            raise
        hint = "Run `irl doctor` to check your system."
        styled_error(exc, hint=hint)
        raise SystemExit(1) from None


def _cli_impl():
    _run_shared_identity_first_run()
    from rich.prompt import Prompt

    from irl.console import console
    from irl.state import load_state, save_state

    state = load_state()
    if _sync_shared_identity_name(state):
        save_state(state)
    if not state.get("name"):
        from irl.keys import is_interactive

        if is_interactive():
            console.print("\n[bold cyan]IRL™ OS Initialization...[/bold cyan]")
            user_name = Prompt.ask("What is your name, organic lifeform?")
            state["name"] = user_name
        else:
            state["name"] = "human"
        save_state(state)
    if not state.get("onboarded_v2"):
        from irl.keys import is_interactive

        if is_interactive():
            _run_onboarding(state)
        else:
            # Piped/CI runs get a silent pass; onboarding deserves a real terminal.
            state["onboarded_v2"] = True
            save_state(state)

    # Easter eggs live before argparse, because argparse has no imagination.
    if len(sys.argv) >= 2:
        egg = sys.argv[1].lower()
        if egg == "42":
            from rich.console import Console

            from irl.ui import accent, panel

            unlocked = unlock_matrix_theme()
            Console().print(
                panel(
                    "[bold]The Answer to the Great Question of Life, the Universe and Everything.[/bold]\n[dim](It is also, coincidentally, the number of packages installed since you woke up.)[/dim]",
                    title=f"[bold {accent()}]irl 42[/bold {accent()}]",
                )
            )
            if unlocked:
                Console().print("[bold bright_green]Wait. What is this? ...The green rain has unlocked something in the store.[/bold bright_green]")
            return
        if egg == "pizza":
            from rich.align import Align
            from rich.console import Console

            from irl.ui import accent

            pizza = r"""
        ___
       |~~~|      ~ pizza delivery for one terminal,
       |~-.|       extra oregano, zero dependencies
       |~~~|
       |_.-|  /\
       |~~~|  ||    [ ready in ~30 min, ships faster than npm ]
       '---'  ^^
"""
            Console().print(Align.center(pizza))
            Console().print(f"[bold {accent()}]Mamma mia. Slices cannot be installed, only earned.[/bold {accent()}]")
            unlock_matrix_theme()
            return

    if len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help"):
        _render_irl_custom_help(state)
        return

    if len(sys.argv) == 1:
        interactive_menu()
        return

    from irl.themes import get_engine

    engine = get_engine()
    _print_irl_wisdom_header(state)

    if os.path.isdir("node_modules"):
        engine.render_node_modules()

    parser = argparse.ArgumentParser(prog="irl", description="IRL™ (In Real Life™) - Software for Humans™.")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    install_parser = subparsers.add_parser("install", help="Get Started")
    install_parser.add_argument("package", help="Name of the package, GitHub repo, or direct URL")

    glasses_parser = subparsers.add_parser("glasses", help="See Clearly")
    glasses_parser.add_argument("package", help="Name of the package to inspect")

    doctor_parser = subparsers.add_parser("doctor", help="Stay Healthy")
    doctor_parser.add_argument("package", help="Name of the package to diagnose")

    subparsers.add_parser("grass", help="Go Outside")
    subparsers.add_parser("posture", help="Fix your posture")
    subparsers.add_parser("window", help="Look outside")
    subparsers.add_parser("mirror", help="Get a compliment")
    subparsers.add_parser("hydrate", help="Drink water")
    subparsers.add_parser("chaos", help="Take the chaos quiz")
    subparsers.add_parser("store", help="Open the IRL store")
    subparsers.add_parser("games", help="Play purchased IRL games")
    subparsers.add_parser("city", help="Enter the IRL City (Economy & Crime)")
    subparsers.add_parser("dashboard", help="Enter Chaotic Dashboard Mode")
    subparsers.add_parser("dash", help="Alias for Chaotic Dashboard Mode")
    manga_parser = subparsers.add_parser("manga", help="Read or Download IRL Manga")
    manga_parser.add_argument("--download", action="store_true", help="Download manga for offline reading")
    manga_parser.add_argument("query", nargs="*", help="Optional manga title search query")
    subparsers.add_parser("story", help="Play the Themed Story Mode")
    subparsers.add_parser("bones", help="Summon Professor Bones for Lofi")
    subparsers.add_parser("joke", help="Tell a random developer joke via JokeAPI")
    subparsers.add_parser("dog", help="Fetch an ASCII dog from Dog API")
    search_parser = subparsers.add_parser("search", help="AI powered package search")
    search_parser.add_argument("query", nargs="+", help="Natural language query to find a package")
    subparsers.add_parser("upgrade", help="Upgrade IRL OS to the latest version")
    rollback_parser = subparsers.add_parser("rollback", help="Roll back IRL OS to an older version")
    rollback_parser.add_argument("version", nargs="?", help="Version to install, e.g. 1.7.1")
    rollback_parser.add_argument("--yes", "-y", action="store_true", help="Rollback without confirmation")
    run_parser = subparsers.add_parser("run", help="Run a command wrapped in IRL OS (e.g. irl run dev)")
    run_parser.add_argument("cmd_args", nargs=argparse.REMAINDER, help="Command and arguments to run")
    subparsers.add_parser("tui", help="Launch the full-screen IRL TUI (needs irl-pkg[tui])")
    subparsers.add_parser("pet", help="Visit your terminal pet")
    subparsers.add_parser("achievements", help="View your achievements and level")
    subparsers.add_parser("quests", help="See today's daily quests")
    subparsers.add_parser("grassland", help="Play Grassland Quest (free garden roguelike)")
    subparsers.add_parser("rhythm", help="Play Lofi Rhythm (beat game with bundled lofi)")
    lang_parser = subparsers.add_parser("lang", help="Run the .irl toy language")
    lang_parser.add_argument("action", nargs="?", choices=["run", "demo", "repl"], default="demo")
    lang_parser.add_argument("file", nargs="?", help=".irl file for `irl lang run <file>`")

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
    elif args.command == "rollback":
        rollback_irl(args.version, args.yes)
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
    elif args.command == "tui":
        from irl.tui_app import run_tui

        run_tui()
    elif args.command == "pet":
        from irl.pet import pet_cli

        pet_cli()
    elif args.command == "achievements":
        from irl.achievements import show_achievements

        show_achievements()
    elif args.command == "quests":
        from irl.quests import show_quests

        show_quests()
    elif args.command == "grassland":
        from irl.grassland_quest import play_grassland_quest

        play_grassland_quest()
    elif args.command == "rhythm":
        from irl.rhythm import play_rhythm

        play_rhythm()
    elif args.command == "lang":
        from irl.lang_runner import run_lang

        run_lang(args.action, args.file)
    else:
        interactive_menu()


def creative_menu():
    from rich.console import Console
    from rich.prompt import IntPrompt

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
    import json
    import os

    from rich.panel import Panel
    from rich.table import Table

    from irl.console import console
    from irl.state import get_global_rank, load_state

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
            with open(grass_file) as f:
                g_state = json.load(f)
                table.add_row("Grass Streak", str(g_state.get("streak", 0)))
        except Exception:
            pass

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
    ("Visit Pet", "Your terminal pet misses you. Probably."),
    ("Daily Quests", "Three tasks a day keep the void away."),
    ("Achievements", "Trophies for surviving software."),
    ("Grassland Quest", "Garden roguelike. Bugs included, literally."),
    ("Lofi Rhythm", "Beat game. Bundled lofi. Bring reflexes."),
    ("Full-screen TUI", "The dashboard, but it moved out and got an app."),
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
        "roast": random.choice(
            [
                "node_modules found. The landfill has become sentient.",
                "Your dependency folder qualifies as a minor geological event.",
                "That is not a folder. That is capitalism with subdirectories.",
                "Disk usage report: emotionally expensive.",
                "The package manager opened a buffet and charged your SSD.",
            ]
        ),
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


_IRL_TIPS = [
    "TIP: `irl doctor <pkg>` checks your system before an install goes sideways.",
    "TIP: `irl glasses <pkg>` shows version, size and source before you commit.",
    "TIP: `irl run dev` in a project folder quietly becomes `npm run dev`.",
    "TIP: Streaks pay. Touch grass daily; your rank climbs, your posture judges you.",
    "TIP: `irl 42` does nothing. Definitely nothing. Definitely no unlock.",
    "TIP: Games pay coins. Coins buy personality. Personality is optional.",
    "TIP: `irl rollback` time-travels your package manager, politely.",
    "TIP: The konami code works on dashboards. On some dashboards. Allegedly.",
    "TIP: `irl tui` is the full-screen mode if you installed the [tui] extra.",
    "TIP: Press Q anywhere in the dashboard. No judgment. Some entries needed.",
]

_stat_cache = {"ts": 0.0, "pip": "?", "npm": "?"}


def _real_stats():
    """Real numbers: package counts and disk, cached for a minute."""
    import json as _json
    import subprocess

    now = time.time()
    if now - _stat_cache["ts"] > 60 and _stat_cache["pip"] == "?":
        try:
            out = subprocess.run(
                [sys.executable, "-m", "pip", "list", "--format", "json", "--disable-pip-version-check"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            _stat_cache["pip"] = str(len(_json.loads(out.stdout or "[]")))
        except Exception:
            _stat_cache["pip"] = "?"
        try:
            out = subprocess.run(["npm", "ls", "-g", "--depth=0"], capture_output=True, text=True, timeout=10)
            _stat_cache["npm"] = str(max(0, out.stdout.count("\n") - 1))
        except Exception:
            _stat_cache["npm"] = "npm?"

    try:
        total, used, free = shutil.disk_usage(os.path.expanduser("~"))
        disk = f"{free / (1024**3):,.0f} GB free"
    except Exception:
        disk = "unknowable"

    stats = {
        "Python": f"{sys.version.split()[0]} (local reality)",
        "pip packages": _stat_cache["pip"],
        "npm globals": _stat_cache["npm"],
        "Home disk": disk,
    }
    return stats


def _grass_heatmap(state):
    """GitHub-style contribution grid of grass touches (last 12 weeks)."""
    from datetime import datetime, timedelta

    from rich.text import Text

    history = state.get("history", {})
    today = datetime.now().date()
    weeks = 12
    cells = []
    for w in range(weeks):
        column = Text()
        for d in range(7):
            day = today - timedelta(days=(weeks - 1 - w) * 7 + (6 - d))
            touched = history.get(day.strftime("%Y-%m-%d"))
            if day == today and state.get("last_touched") == day.strftime("%Y-%m-%d"):
                column.append(" ▪", style="bold bright_green")
            elif touched:
                column.append(" ▪", style="green")
            else:
                column.append(" ·", style=f"dim {IRL_MUTED}")
        cells.append(column)
    title = Text(f" GRASS STREAK: {state.get('streak', 0)} days ", style="bold green")
    grid = Table.grid(padding=0)
    for _ in range(weeks):
        grid.add_column()
    grid.add_row(*cells)
    return Panel(grid, title=title, border_style=IRL_BORDER, box=box.SQUARE)


def _build_dashboard(state, rank, user_name, tick, selected=0):
    from irl.themes import get_engine
    from irl.themes.layouts import DASHBOARD_SKINS, render_dashboard_chrome

    engine = get_engine()
    skin = DASHBOARD_SKINS.get(engine.color_id, DASHBOARD_SKINS["default"])
    accent = skin["accent"]
    border = skin["border"]
    theme_box = skin["box"]

    node = _node_modules_report()
    stats = _real_stats()
    grass_state_path = os.path.expanduser("~/.irl_grass.json")
    grass_state = {}
    try:
        with open(grass_state_path) as f:
            grass_state = json.load(f)
    except Exception:
        grass_state = {"streak": 0, "history": {}}

    ticker_offset = tick % len(CHAOS_TICKERS)
    ticker = "  //  ".join(CHAOS_TICKERS[ticker_offset:] + CHAOS_TICKERS[:ticker_offset])
    if tick % 2 == 0:
        ticker = _IRL_TIPS[(tick // 2) % len(_IRL_TIPS)]

    menu = Table.grid(expand=True)
    menu.add_column(ratio=1)
    for idx, (label, desc) in enumerate(CHAOS_TASKS, start=1):
        if idx - 1 == selected:
            style = f"bold black on {accent}"
            cursor = ">"
        else:
            style = f"bold {border}"
            cursor = " "
        menu.add_row(f"[{style}] {cursor} {idx:02}. {label}[/] [dim]{desc}[/dim]")

    menu.add_row("")
    menu.add_row(f"[{accent}]CONTROLS: \\[W]/\\[S] or \\[UP]/\\[DOWN] to scroll • \\[ENTER] to select • \\[Q] to exit[/{accent}]")

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
        Layout(name="heatmap", size=9),
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
    layout["heatmap"].update(_grass_heatmap(grass_state))

    # Use theme colors for the ticker
    ticker_text = f"[bold {border}]IRL SIGNAL FEED[/bold {border}]"
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
    elif choice == 17:
        from irl.pet import pet_cli

        pet_cli()
    elif choice == 18:
        from irl.quests import show_quests

        show_quests()
    elif choice == 19:
        from irl.achievements import show_achievements

        show_achievements()
    elif choice == 20:
        from irl.grassland_quest import play_grassland_quest

        play_grassland_quest()
    elif choice == 21:
        from irl.rhythm import play_rhythm

        play_rhythm()
    elif choice == 22:
        from irl.tui_app import run_tui

        run_tui()
    return True


def chaotic_dashboard_mode(loop=False):
    from rich.prompt import Prompt

    from irl.console import console
    from irl.keys import (
        KEY_CTRL_C,
        KEY_DOWN,
        KEY_ENTER,
        KEY_ESC,
        KEY_SPACE,
        KEY_UP,
        flush_keys,
        is_interactive,
        kbhit,
        read_key,
    )
    from irl.state import get_global_rank, load_state

    if not is_interactive():
        # No terminal to draw on (piped/CI): offer the numbered menu instead.
        user_name = load_state().get("name", "human")
        console.print(f"[bold {IRL_ACCENT}]IRL™ Dashboard (compact mode — pipe detected)[/bold {IRL_ACCENT}]")
        table = Table(show_header=False, box=None, expand=True, pad_edge=False)
        table.add_column("No", style=f"bold {IRL_MUTED}", no_wrap=True)
        table.add_column("Task", style=f"bold {IRL_ACCENT}", no_wrap=True)
        for idx, (label, desc) in enumerate(CHAOS_TASKS, start=1):
            table.add_row(f"[{idx}]", f"{label} — {desc}")
        console.print(table)
        raw = Prompt.ask("Pick a task number (0 to leave)", default="0").strip()
        try:
            chosen = int(raw)
        except ValueError:
            chosen = 0
        if chosen <= 0 or chosen > len(CHAOS_TASKS):
            return
        _dispatch_dashboard_choice(chosen)
        return

    while True:
        state = load_state()
        user_name = state.get("name", "human")
        rank = get_global_rank(state)
        selected = 0

        # ROBUST FLUSH: Terminals can take a split second to send the Enter key
        # that was used to launch the command. We must wait and flush completely.
        end_flush = time.time() + 0.35
        while time.time() < end_flush:
            flush_keys()
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
                konami = False
                recent = []
                KONAMI = ["UP", "UP", "DOWN", "DOWN", "LEFT", "RIGHT", "LEFT", "RIGHT", "b", "a"]

                while True:
                    live.update(_build_dashboard(state, rank, user_name, tick, selected))
                    time.sleep(0.1)  # 10 FPS animation
                    tick += 1

                    while kbhit():
                        try:
                            key = read_key()
                        except EOFError:
                            chosen = 0
                            break
                        # --- konami watch (some locks open from the inside) ---
                        recent.append(key.char.lower() if key.is_char() and key.char else key.name)
                        recent[:] = recent[-10:]
                        if recent == KONAMI:
                            konami = True
                            chosen = 0
                            break
                        if key in (KEY_UP,):
                            selected = (selected - 1) % len(CHAOS_TASKS)
                        elif key in (KEY_DOWN,):
                            selected = (selected + 1) % len(CHAOS_TASKS)
                        elif key.is_char("w"):
                            selected = (selected - 1) % len(CHAOS_TASKS)
                        elif key.is_char("s"):
                            selected = (selected + 1) % len(CHAOS_TASKS)
                        elif key in (KEY_ENTER, KEY_SPACE):
                            chosen = selected + 1
                            break
                        elif key.is_char("0"):
                            chosen = 0
                            break
                        elif key.is_char("q") or key in (KEY_ESC, KEY_CTRL_C):
                            chosen = 0
                            break

                    if chosen is not None:
                        break

        if chosen == 0:
            if konami:
                unlock_matrix_theme()
                console.print(
                    Panel(
                        "[bold bright_green]There is no spoon. There is no lock.[/bold bright_green]\n\n"
                        "A new theme has appeared in your collection. You already know which one.\n"
                        "[dim]Check the store, or just look at the rain. It is green now.[/dim]",
                        border_style="green",
                    )
                )
            break

        keep_going = _dispatch_dashboard_choice(chosen)
        if not loop or not keep_going:
            break


def interactive_menu():
    from rich.prompt import Prompt
    from rich.table import Table

    from irl.state import load_state

    state = load_state()

    visible_commands = [item for item in IRL_COMMANDS if item[0] != "exit"]
    table = Table(show_header=False, box=None, expand=True, pad_edge=False)
    table.add_column("No", style=f"bold {IRL_MUTED}", no_wrap=True)
    table.add_column("Command", style=f"bold {IRL_ACCENT}", no_wrap=True)
    table.add_column("Description", style=IRL_CREAM)
    aliases = {}
    for index, (cmd, desc, value) in enumerate(visible_commands, start=1):
        table.add_row(f"[{index}]", f"/{cmd:<11}", desc)
        aliases[str(index)] = value
        aliases[cmd] = value
        aliases[f"/{cmd}"] = value
    c = _print_irl_wisdom_header(state)
    c.print(table)
    c.print(f"[{IRL_MUTED}]Type a number or slash command. Example: /rollback[/{IRL_MUTED}]")
    raw_choice = Prompt.ask(f"[{IRL_CREAM}]Choose command[/{IRL_CREAM}]", default="dashboard").strip()
    choice = aliases.get(raw_choice.lower(), raw_choice.lower().lstrip("/"))

    if not choice or choice == "exit":
        return
    if choice in ("install", "glasses", "doctor"):
        from rich.console import Console

        c = Console(highlight=False)
        prompt = {"install": "Package name, repo, or URL", "glasses": "Package to inspect", "doctor": "Package to diagnose"}[choice]
        target = Prompt.ask(f"[{IRL_CREAM}]{prompt}[/{IRL_CREAM}]")
        if not target:
            return
        if choice == "install":
            install_package(target)
        elif choice == "glasses":
            inspect_package(target)
        else:
            run_doctor(target)
        return
    if choice == "search":
        query = Prompt.ask(f"[{IRL_CREAM}]What package are you looking for?[/{IRL_CREAM}]")
        if query:
            from irl.search import search_and_install

            search_and_install(query)
        return
    mapping = {
        "dashboard": 0,
        "grass": 4,
        "store": 6,
        "games": 8,
        "upgrade": 10,
        "city": 11,
        "manga": 12,
        "story": 13,
        "bones": 14,
        "joke": 15,
        "dog": 16,
        "pet": 17,
        "quests": 18,
        "achievements": 19,
        "grassland": 20,
        "rhythm": 21,
        "tui": 22,
    }
    if choice == "rollback":
        rollback_irl()
    elif choice == "posture":
        from irl.creative import posture

        posture()
    elif choice == "hydrate":
        from irl.creative import hydrate

        hydrate()
    elif choice == "dashboard":
        chaotic_dashboard_mode(loop=True)
    elif choice in mapping:
        _dispatch_dashboard_choice(mapping[choice])


if __name__ == "__main__":
    cli()
