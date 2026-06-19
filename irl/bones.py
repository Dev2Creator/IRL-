# IRL™ 🌱 - Software for Humans

import time
import os
import ctypes
from urllib.request import urlretrieve
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from irl.console import console

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
    panel = Panel(
        Align.center(msg4),
        border_style="cyan",
        box=__import__("rich.box").box.DOUBLE_EDGE,
        padding=(1, 5)
    )
    console.print(panel)
    
    # Use a direct public MP3 link
    mp3_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    temp_dir = os.environ.get("TEMP", "C:\\Temp")
    temp_file = os.path.join(temp_dir, "irl_flamenco.mp3")
    
    try:
        with console._console.status("[dim]Pulling audio stream directly from web...[/dim]"):
            if not os.path.exists(temp_file):
                urlretrieve(mp3_url, temp_file)
        
        # Play directly in terminal via Windows MCI without opening any external apps
        ctypes.windll.winmm.mciSendStringW(f'open "{temp_file}" type mpegvideo alias flamenco', None, 0, None)
        ctypes.windll.winmm.mciSendStringW('play flamenco', None, 0, None)
        
        console.print(Align.center(Text("(Audio playing directly in terminal... Press Ctrl+C to stop)", style="dim italic")))
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            ctypes.windll.winmm.mciSendStringW('stop flamenco', None, 0, None)
            ctypes.windll.winmm.mciSendStringW('close flamenco', None, 0, None)
            console.print("\n[bold red]Bones returns to the grave...[/bold red]")
            
    except Exception as e:
        console.print(f"[bold red]Failed to stream audio: {e}[/bold red]")
