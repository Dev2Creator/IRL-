# IRL™ 🌱 - Software for Humans

import requests
from rich.panel import Panel
from rich.align import Align
from irl.console import console

def tell_joke():
    try:
        with console._console.status("[dim cyan]Contacting v2.jokeapi.dev...[/dim cyan]"):
            resp = requests.get("https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Pun?blacklistFlags=nsfw,religious,political,racist,sexist,explicit", timeout=5, verify=False)
            resp.raise_for_status()
            data = resp.json()
            
        if data.get("type") == "single":
            joke = data.get("joke")
        else:
            joke = f"{data.get('setup')}\n\n[dim italic]... {data.get('delivery')}[/dim italic]"
            
        console.print()
        console.print(Panel(Align.center(f"\n{joke}\n"), title="[bold magenta]JokeAPI 🤡[/bold magenta]", border_style="cyan"))
        console.print()
        
    except Exception as e:
        console.print(f"[bold red]Failed to fetch joke. Your ISP probably blocked it![/bold red]\n[dim]{e}[/dim]")
