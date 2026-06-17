# IRL™ 🌱 - Software for Humans

from rich.console import Group
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from irl.console import console
import time

MANGA_CHAPTERS = [
    {
        "title": "Chapter 1: That Time I Got Reincarnated as a Node Module",
        "panels": [
            "[bold white]Where am I...? It's so dark... and heavy.[/bold white]\n\n[dim](*MENACING SFX: ｺﾞｺﾞｺﾞｺﾞ*)[/dim]",
            "[bold pink1]Senpai! Look out! The circular dependency is attacking![/bold pink1]\n\n[red]N-NANI?![/red]",
            "[yellow]I must use my ultimate move: `npm audit fix --force`![/yellow]\n\n[bold red]*KABOOOM*[/bold red]\n(The entire production environment collapses)"
        ]
    },
    {
        "title": "Chapter 2: Attack on Production",
        "panels": [
            "[bold white]On that day, developers received a grim reminder...[/bold white]\n\n[dim]We lived in fear of the Friday Deploy.[/dim]",
            "[red]The server wall has been breached! The 500 errors are getting in![/red]\n\n[bold magenta]SASAGEYO! SASAGEYO![/bold magenta] (DevOps team screaming)",
            "[bold cyan]Captain Levi (Senior Dev):[/bold cyan]\n'Just rollback to the previous commit, you idiots.'\n\n[green]*SWISH*[/green] (The servers stabilize)"
        ]
    },
    {
        "title": "Chapter 3: Jojo's Bizarre Architecture",
        "panels": [
            "[bold purple]Tech Lead:[/bold purple] 'Oh? You're approaching me? Instead of writing tests, you're coming right to me?'\n\n[dim]*MENACING SFX: ｺﾞｺﾞｺﾞｺﾞ*[/dim]",
            "[bold yellow]Junior Dev:[/bold yellow] 'I can't push to master without getting closer!'",
            "[bold purple]Tech Lead:[/bold purple] 'MUDA MUDA MUDA! Your code is full of memory leaks!'\n\n[bold yellow]Junior Dev:[/bold yellow] 'ORA ORA ORA! I used Rust!'\n\n[dim](The tech lead is defeated by memory safety)[/dim]"
        ]
    }
]

def read_manga():
    console.print("\n[bold magenta]🌸 IRL™ MANGA READER 🌸[/bold magenta]")
    
    for idx, chapter in enumerate(MANGA_CHAPTERS, start=1):
        console.print(f"  [bold cyan]{idx}.[/bold cyan] {chapter['title']}")
        
    from rich.prompt import IntPrompt
    choice = IntPrompt.ask(
        "Select a chapter to read",
        choices=[str(i) for i in range(1, len(MANGA_CHAPTERS) + 1)],
        console=console._console
    )
    
    chapter = MANGA_CHAPTERS[choice - 1]
    console.print(f"\n[bold white on black] --- {chapter['title']} --- [/bold white on black]\n")
    
    for panel_text in chapter["panels"]:
        panel = Panel(
            Align.center(panel_text),
            box=__import__("rich.box").box.HEAVY_EDGE,
            border_style="white",
            padding=(1, 5)
        )
        console.print(panel)
        time.sleep(2)
        
    console.print("\n[bold red]< TO BE CONTINUED /|\\ [/bold red]\n")
