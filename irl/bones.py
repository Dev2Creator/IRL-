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

import os
import tempfile
import time
from urllib.request import urlretrieve

from rich.align import Align
from rich.box import DOUBLE_EDGE
from rich.panel import Panel
from rich.text import Text

from irl.audio import play_mp3, stop_audio
from irl.console import console

BONES_MP3_URL = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"


def summon_bones():
    console.print()

    msg1 = Text("☠ Professor Bones awakens...", style="bold white on black")
    console.print(Align.center(msg1))
    time.sleep(2)

    msg2 = Text("Rattling skeleton noises detected.", style="dim italic white")
    console.print(Align.center(msg2))
    time.sleep(1.5)

    msg3 = Text("Loading cassette tape...", style="bold green")
    console.print(Align.center(msg3))
    time.sleep(2)

    msg4 = Text("Now Playing:\nFlamenco Beats to Compile Code To", style="bold cyan")
    panel = Panel(Align.center(msg4), border_style="cyan", box=DOUBLE_EDGE, padding=(1, 5))
    console.print(panel)

    temp_file = os.path.join(tempfile.gettempdir(), "irl_flamenco.mp3")

    try:
        with console._console.status("[dim]Pulling audio stream directly from web...[/dim]"):
            if not os.path.exists(temp_file):
                urlretrieve(BONES_MP3_URL, temp_file)

        if not play_mp3(temp_file):
            console.print("[yellow]💀 No audio backend found (tried winmm/ffplay/afplay/paplay). Bones plays air guitar instead.[/yellow]")
            return

        console.print(Align.center(Text("(Audio playing directly in terminal... Press Ctrl+C to stop)", style="dim italic")))
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            stop_audio()
            console.print("\n[bold red]Bones returns to the grave...[/bold red]")

    except Exception as e:
        console.print(f"[bold red]Failed to stream audio: {e}[/bold red]")
