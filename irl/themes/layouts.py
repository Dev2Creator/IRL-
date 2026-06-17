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

import time
import random
import sys
import json
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich import box

from irl.themes.base import BaseLayout

console = Console()

class DefaultLayout(BaseLayout):
    def render_banner(self):
        console.print(Panel("Welcome to IRL™", border_style="blue"))
        
    def render_grass(self, text):
        console.print(f"[green]🌿 {text}[/green]")
        
    def render_hydrate(self, text, glasses):
        console.print(f"[cyan]💧 {text} ({glasses} glasses)[/cyan]")
        
    def render_install(self, text):
        console.print(f"[yellow]📦 {text}[/yellow]")
        
    def render_coin_gain(self, amount, msg):
        console.print(f"[gold1]💰 +{amount} coins: {msg}[/gold1]")
        
    def render_generic(self, text):
        console.print(text)

    def render_node_modules(self, text):
        console.print(f"[bold red]📦 {text}[/bold red]")
        
    def render_run_start(self, text):
        console.print(f"[bold yellow]⚡ {text}[/bold yellow]")
        
    def render_run_success(self, text):
        console.print(f"[bold green]✅ {text}[/bold green]")

class HackerLayout(BaseLayout):
    def _hex_dump(self):
        return "".join(random.choices("0123456789ABCDEF", k=8))
        
    def _print_hacker(self, text):
        for line in text.split('\n'):
            console.print(f"[bold green]0x{self._hex_dump()}  {line}[/bold green]")
            time.sleep(0.05)

    def render_banner(self):
        self._print_hacker("INITIALIZING IRL™ OS...\nSYSTEM COMPROMISED. ENJOY.")
        
    def render_grass(self, text):
        self._print_hacker(f"EXECUTE: touch_grass.sh -> {text}")
        
    def render_hydrate(self, text, glasses):
        self._print_hacker(f"MEM_ALLOC: hydrate() -> {glasses} units -> {text}")
        
    def render_install(self, text):
        self._print_hacker(f"APT-GET INSTALL: {text}")
        
    def render_coin_gain(self, amount, msg):
        self._print_hacker(f"CRYPT_MINER: +{amount} BTC [msg: {msg}]")
        
    def render_generic(self, text):
        self._print_hacker(f"SYS_MSG: {text}")

    def render_node_modules(self, text):
        self._print_hacker(f"WARNING: VULNERABILITY DETECTED -> {text}")

    def render_run_start(self, text):
        self._print_hacker(f"EXEC_INIT: {text}")

    def render_run_success(self, text):
        self._print_hacker(f"EXEC_SUCCESS: {text}")

class CyberpunkLayout(BaseLayout):
    def render_banner(self):
        console.print(Panel("[bold cyan]N I G H T   C I T Y[/bold cyan]", border_style="magenta", box=box.HEAVY))
        
    def render_grass(self, text):
        console.print(f"[bold magenta]SYNTH-GRASS DETECTED // [/bold magenta][yellow]{text}[/yellow]")
        
    def render_hydrate(self, text, glasses):
        console.print(f"[bold cyan]HYDRATION IMPLANT ACTIVATED // [/bold cyan][white]{glasses} VIALS // {text}[/white]")
        
    def render_install(self, text):
        console.print(f"[bold yellow]DOWNLOADING CYBERWARE // [/bold yellow][magenta]{text}[/magenta]")
        
    def render_coin_gain(self, amount, msg):
        console.print(f"[bold green]CREDITS TRANSFERRED: +{amount} EDDIES // {msg}[/bold green]")
        
    def render_generic(self, text):
        console.print(f"[bold cyan]> [/bold cyan][white]{text}[/white]")

    def render_node_modules(self, text):
        console.print(f"[bold red]MALWARE SCAN: [/bold red][yellow]{text}[/yellow]")

    def render_run_start(self, text):
        console.print(f"[bold yellow]RUNNING SCRIPT // [/bold yellow][white]{text}[/white]")

    def render_run_success(self, text):
        console.print(f"[bold green]SCRIPT COMPLETE // [/bold green][white]{text}[/white]")

class DraculaLayout(BaseLayout):
    def render_banner(self):
        console.print(Panel("[bold red]Welcome to the Night, Child.[/bold red]", border_style="purple", box=box.DOUBLE))
        
    def render_grass(self, text):
        console.print(f"[purple]The dead grass crunches...[/purple] [red]{text}[/red]")
        
    def render_hydrate(self, text, glasses):
        console.print(f"[red]Drinking the crimson essence... ({glasses} goblets)[/red] [white]{text}[/white]")
        
    def render_install(self, text):
        console.print(f"[purple]Summoning dark artifact...[/purple] [black on red]{text}[/black on red]")
        
    def render_coin_gain(self, amount, msg):
        console.print(f"[bold red]Blood tithe collected: +{amount}[/bold red] [purple]{msg}[/purple]")
        
    def render_generic(self, text):
        console.print(f"[white on black]🦇 {text} 🦇[/white on black]")

    def render_node_modules(self, text):
        console.print(f"[black on red]The darkness grows...[/black on red] [purple]{text}[/purple]")

    def render_run_start(self, text):
        console.print(f"[purple]Awakening the script...[/purple] [red]{text}[/red]")

    def render_run_success(self, text):
        console.print(f"[bold red]The deed is done...[/bold red] [purple]{text}[/purple]")

class AnimeLayout(BaseLayout):
    def render_banner(self):
        console.print(Panel("[bold pink1]✨ Welcome to IRL™, Senpai! ✨[/bold pink1]", border_style="hot_pink", box=box.ROUNDED))
        
    def render_grass(self, text):
        console.print(f"[green]UwU *touches grass*[/green] [pink1]{text}[/pink1] (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
        
    def render_hydrate(self, text, glasses):
        console.print(f"[cyan]Oishii water! *glug glug* ({glasses})[/cyan] [pink1]{text}[/pink1] 💧( ˘▽˘)っ♨")
        
    def render_install(self, text):
        console.print(f"[yellow]Sugoi! New module installing~[/yellow] [pink1]{text}[/pink1] ✨( ✯◡✯)")
        
    def render_coin_gain(self, amount, msg):
        console.print(f"[gold1]YATTA! +{amount} coins! ({msg})[/gold1] 💰(≧◡≦)")
        
    def render_generic(self, text):
        console.print(f"[pink1]{text} ~nyan[/pink1] 🐾")

    def render_node_modules(self, text):
        console.print(f"[bold red]KYAA! [/bold red][pink1]{text}[/pink1] (｡>﹏<｡)")

    def render_run_start(self, text):
        console.print(f"[yellow]Ikuzo! [/yellow][pink1]{text}[/pink1] ✧*｡٩(ˊᗜˋ*)و✧*｡")

    def render_run_success(self, text):
        console.print(f"[bold green]Sugoi! [/bold green][pink1]{text}[/pink1] (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")

class CryptoLayout(BaseLayout):
    def render_banner(self):
        table = Table(title="IRL™ MARKET STATUS", show_header=True, header_style="bold magenta")
        table.add_column("Asset", style="cyan")
        table.add_column("Trend", justify="right", style="green")
        table.add_row("$IRL™", "🚀 MOONING")
        console.print(table)
        
    def render_grass(self, text):
        console.print(f"[bold green]📈 GRASS/USD LONG POSITION OPENED: {text}[/bold green]")
        
    def render_hydrate(self, text, glasses):
        console.print(f"[bold cyan]💧 LIQUIDITY POOL ADDED: {glasses} GLASSES. {text}[/bold cyan]")
        
    def render_install(self, text):
        console.print(f"[bold yellow]⛓ SMART CONTRACT DEPLOYED: {text}[/bold yellow]")
        
    def render_coin_gain(self, amount, msg):
        console.print(f"[bold green]💎🙌 AIRDROP: +{amount} TOKENS ({msg})[/bold green]")
        
    def render_generic(self, text):
        console.print(f"[white]BLOCKCHAIN EVENT: {text}[/white]")

    def render_node_modules(self, text):
        console.print(f"[bold red]📉 PORTFOLIO DUMP: {text}[/bold red]")

    def render_run_start(self, text):
        console.print(f"[bold yellow]⏳ PENDING TX: {text}[/bold yellow]")

    def render_run_success(self, text):
        console.print(f"[bold green]✅ TX CONFIRMED: {text}[/bold green]")

class PirateLayout(BaseLayout):
    def render_banner(self):
        console.print(Panel("[bold yellow]⚓ Yarr! Welcome aboard the good ship IRL™! ⚓[/bold yellow]", border_style="red", box=box.ASCII))
        
    def render_grass(self, text):
        console.print(f"[green]🌿 Foot on dry land! {text}[/green]")
        
    def render_hydrate(self, text, glasses):
        console.print(f"[cyan]🍺 Down the hatch! {glasses} tankards of fresh water. {text}[/cyan]")
        
    def render_install(self, text):
        console.print(f"[yellow]📦 Hoisting new cargo: {text}[/yellow]")
        
    def render_coin_gain(self, amount, msg):
        console.print(f"[gold1]💰 Shiver me timbers! +{amount} doubloons! ({msg})[/gold1]")
        
    def render_generic(self, text):
        console.print(f"[white]🦜 {text}[/white]")

    def render_node_modules(self, text):
        console.print(f"[red]Kraken ahead! {text}[/red]")

    def render_run_start(self, text):
        console.print(f"[yellow]Load the cannons! {text}[/yellow]")

    def render_run_success(self, text):
        console.print(f"[green]Direct hit! {text}[/green]")

class EldritchLayout(BaseLayout):
    def _zalgo(self, text):
        zalgo_chars = [chr(i) for i in range(0x0300, 0x036F + 1)]
        result = ""
        for c in text:
            result += c
            for _ in range(random.randint(1, 3)):
                result += random.choice(zalgo_chars)
        return result

    def render_banner(self):
        console.print(Panel(self._zalgo("THE OLD ONES AWAKEN"), border_style="red", style="bold red"))
        
    def render_grass(self, text):
        console.print(f"[green]{self._zalgo('Tainted flora touched: ')}[/green][dark_green]{text}[/dark_green]")
        
    def render_hydrate(self, text, glasses):
        console.print(f"[cyan]{self._zalgo('Drinking from the abyss (')} {glasses} {self._zalgo(')')}[/cyan] [blue]{text}[/blue]")
        
    def render_install(self, text):
        console.print(f"[magenta]{self._zalgo('A new terror manifests: ')} {text}[/magenta]")
        
    def render_coin_gain(self, amount, msg):
        console.print(f"[red]{self._zalgo('Souls harvested: +')}{amount}[/red] [dark_red]({msg})[/dark_red]")
        
    def render_generic(self, text):
        console.print(self._zalgo(text), style="dim white")

    def render_node_modules(self, text):
        console.print(f"[bold red]{self._zalgo('Madness approaches: ')}[/bold red][dark_red]{text}[/dark_red]")

    def render_run_start(self, text):
        console.print(f"[magenta]{self._zalgo('Chanting: ')}[/magenta][purple]{text}[/purple]")

    def render_run_success(self, text):
        console.print(f"[bold green]{self._zalgo('Ritual complete: ')}[/bold green][dark_green]{text}[/dark_green]")

class BoomerLayout(BaseLayout):
    def _slow_print(self, text):
        text = text.upper()
        # Amber coloring
        sys.stdout.write("\033[38;2;255;191;0m")
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.015)
        sys.stdout.write("\033[0m\n")

    def render_banner(self):
        self._slow_print("--- BACK IN MY DAY WE DIDN'T HAVE THESE FANCY APPS ---")
        
    def render_grass(self, text):
        self._slow_print(f"FINALLY WENT OUTSIDE. {text}. KIDS THESE DAYS JUST LOOK AT SCREENS.")
        
    def render_hydrate(self, text, glasses):
        self._slow_print(f"DRANK WATER FROM THE HOSE. {glasses} GLASSES. {text}. BUILDS CHARACTER.")
        
    def render_install(self, text):
        self._slow_print(f"HOW DO I INSTALL {text}? WHERE IS THE FLOPPY DISK?")
        
    def render_coin_gain(self, amount, msg):
        self._slow_print(f"FOUND {amount} PENNIES ON THE STREET. {msg}. A PENNY SAVED IS A PENNY EARNED.")
        
    def render_generic(self, text):
        self._slow_print(text)

    def render_node_modules(self, text):
        console.print(f"[bold red]BACK IN MY DAY! {text}[/bold red]")

    def render_run_start(self, text):
        console.print(f"[yellow]STARTING UP... {text}[/yellow]")

    def render_run_success(self, text):
        console.print(f"[bold green]FINALLY DONE. {text}[/bold green]")

class ZenLayout(BaseLayout):
    def render_banner(self):
        console.print(Align.center("[dim white]Breathe in. Breathe out. Welcome to IRL™.[/dim white]"))
        
    def render_grass(self, text):
        console.print(Align.center(f"[dim green]Nature connects us all. {text}[/dim green]"))
        
    def render_hydrate(self, text, glasses):
        console.print(Align.center(f"[dim cyan]Be like water. ({glasses} glasses) {text}[/dim cyan]"))
        
    def render_install(self, text):
        console.print(Align.center(f"[dim yellow]A new tool joins your practice: {text}[/dim yellow]"))
        
    def render_coin_gain(self, amount, msg):
        console.print(Align.center(f"[dim white]Abundance flows to you: +{amount}. {msg}[/dim white]"))
        
    def render_generic(self, text):
        console.print(Align.center(f"[dim white]{text}[/dim white]"))

    def render_node_modules(self, text):
        console.print(f"[dim white]Imbalance... {text}[/dim white]")

    def render_run_start(self, text):
        console.print(f"[white]Beginning... {text}[/white]")

    def render_run_success(self, text):
        console.print(f"[dim white]Ended... {text}[/dim white]")

class ToxicLayout(BaseLayout):
    def _rainbow_text(self, text):
        colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
        result = Text()
        for i, char in enumerate(text):
            result.append(char, style=f"bold {colors[i % len(colors)]} blink")
        return result

    def render_banner(self):
        console.print(Panel(self._rainbow_text("!!! GET REKT NOOB !!! WELCOME TO IRL™ !!!"), box=box.HEAVY))
        
    def render_grass(self, text):
        console.print(self._rainbow_text(f"TOUCH GRASS YOU SWEAT! 🌿 💀 {text}"))
        
    def render_hydrate(self, text, glasses):
        console.print(self._rainbow_text(f"STAY MAD, STAY HYDRATED! 💧 {glasses} GLASSES! {text}"))
        
    def render_install(self, text):
        console.print(self._rainbow_text(f"INSTALLING VIRUS... JK LOL IT'S {text} 🤡"))
        
    def render_coin_gain(self, amount, msg):
        console.print(self._rainbow_text(f"EZ MONEY +{amount} 🤑 RATIO + L + {msg}"))
        
    def render_generic(self, text):
        console.print(self._rainbow_text(f"🤡 {text} 🤡"))

    def render_node_modules(self, text):
        console.print(f"[bold red]LMAO TRASH: {text}[/bold red]")

    def render_run_start(self, text):
        console.print(f"[yellow]Trying and failing: {text}[/yellow]")

    def render_run_success(self, text):
        console.print(f"[bold green]Lucky guess: {text}[/bold green]")

class AILayout(BaseLayout):
    def render_banner(self):
        data = {"event": "system_init", "status": "online", "model": "IRL™-1.0"}
        console.print(f"[bold blue]SystemPrompt:[/bold blue] [dim]{json.dumps(data, indent=2)}[/dim]")
        
    def render_grass(self, text):
        console.print(f"[bold magenta]Action/Execute:[/bold magenta] tool_name=touch_grass, text={text}")
        
    def render_hydrate(self, text, glasses):
        console.print(f"[bold magenta]Action/Execute:[/bold magenta] tool_name=hydrate, glasses={glasses}, text={text}")
        
    def render_install(self, text):
        console.print(f"[bold magenta]Action/Execute:[/bold magenta] tool_name=install_module, name={text}")
        
    def render_coin_gain(self, amount, msg):
        console.print(f"[bold green]Observation/Reward:[/bold green] +{amount} (reasoning: {msg})")
        
    def render_generic(self, text):
        console.print(f"[bold cyan]Response:[/bold cyan] {text}")


DASHBOARD_SKINS = {
    "default": {"title": "IRL™ CORPORATE PANIC DESK", "border": "blue", "accent": "cyan", "box": box.ROUNDED, "art": "KPI: Still Employed"},
    "hacker": {"title": "ROOT@BASEMENT:~# IRL_OVERRIDE", "border": "green", "accent": "bright_green", "box": box.HEAVY, "art": "01001001 01010010 01001100"},
    "cyberpunk": {"title": "NEON DAMAGE CONTROL // NIGHT CITY", "border": "magenta", "accent": "cyan", "box": box.DOUBLE, "art": "CORPO BURNOUT INTERFACE"},
    "dracula": {"title": "CASTLE CI/CD: BLOOD PIPELINE", "border": "red", "accent": "purple", "box": box.DOUBLE_EDGE, "art": "legacy code never dies"},
    "anime": {"title": "IRL-CHAN CHAOS CONTROL DESU", "border": "hot_pink", "accent": "pink1", "box": box.ROUNDED, "art": "senpai your build is cursed"},
    "crypto": {"title": "$IRL TERMINAL EXCHANGE", "border": "yellow", "accent": "green", "box": box.HEAVY_HEAD, "art": "HOPE/USD -99.7% | COPIUM +420%"},
    "pirate": {"title": "THE BLACK TERMINAL", "border": "yellow", "accent": "red", "box": box.ASCII_DOUBLE_HEAD, "art": "yarr, here be dependencies"},
    "eldritch": {"title": "THE UNSPEAKABLE DASHBOARD", "border": "dark_red", "accent": "magenta", "box": box.HEAVY_EDGE, "art": "THE LOGS ARE CHANTING"},
    "boomer": {"title": "MAINFRAME OF DISAPPOINTMENT", "border": "yellow", "accent": "bright_yellow", "box": box.ASCII, "art": "BACK WHEN RAM WAS EARNED, NOT ALLOCATED"},
    "zen": {"title": "VOID OPS", "border": "white", "accent": "dim cyan", "box": box.MINIMAL, "art": "the bug is temporary. the suffering is versioned."},
    "toxic": {"title": "RANKED TERMINAL LOBBY", "border": "bright_red", "accent": "bright_magenta", "box": box.HEAVY, "art": "RATIO + L + UNHANDLED EXCEPTION"},
    "ai": {"title": "MODEL_CONTEXT_PROTOCOL: DESPAIR", "border": "bright_blue", "accent": "bright_cyan", "box": box.SQUARE, "art": '{"status":"online","ethics":"pending","vibes":"compiled"}'},
}


def render_dashboard_chrome(kind, theme_id, payload, meta=None, tick=0):
    skin = DASHBOARD_SKINS.get(theme_id, DASHBOARD_SKINS["default"])
    pulse = "!" * ((tick % 3) + 1)

    if kind == "header":
        content = Group(
            Align.center(Text(skin["art"], style=f"bold {skin['accent']}")),
            Align.center(Text(f"{skin['title']} {pulse}", style=f"bold {skin['accent']}")),
            Align.center(Text(f"operator={payload} rank={meta} refresh={tick}", style="dim")),
        )
        return Panel(content, border_style=skin["border"], box=skin["box"])

    if kind == "menu":
        return Panel(payload, title=f"[bold {skin['accent']}]COMMAND MENU[/bold {skin['accent']}]", subtitle="[dim]choose a bad idea professionally[/dim]", border_style=skin["border"], box=skin["box"])

    if kind == "stats":
        return Panel(payload, title=f"[bold {skin['accent']}]FAKE SYSTEM VITALS[/bold {skin['accent']}]", border_style=skin["border"], box=skin["box"])

    if kind == "node":
        return Panel(Group(payload, Text(str(meta), style="bold red")), title=f"[bold {skin['accent']}]DEPENDENCY LANDFILL SCAN[/bold {skin['accent']}]", border_style=skin["border"], box=skin["box"])

    if kind == "ticker":
        return Panel(Text(str(payload), style=f"bold {skin['accent']}"), title="[bold red]DARK HUMOR INCIDENT FEED[/bold red]", border_style=skin["border"], box=skin["box"])

    return Panel(str(payload), border_style=skin["border"], box=skin["box"])

LAYOUTS = {
    'default': DefaultLayout,
    'hacker': HackerLayout,
    'cyberpunk': CyberpunkLayout,
    'dracula': DraculaLayout,
    'anime': AnimeLayout,
    'crypto': CryptoLayout,
    'pirate': PirateLayout,
    'eldritch': EldritchLayout,
    'boomer': BoomerLayout,
    'zen': ZenLayout,
    'toxic': ToxicLayout,
    'ai': AILayout
}
