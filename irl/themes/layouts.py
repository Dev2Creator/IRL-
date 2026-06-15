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
from rich.console import Console
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
