import os
import json
import random
import requests
from datetime import datetime
from rich.console import Console

console = Console()

WATER_STATE_FILE = os.path.expanduser("~/.irl_water.json")

def posture():
    shrimp = r"""
       🦐
     / | \
    """
    console.print(f"[bold red]{shrimp}[/bold red]")
    console.print("[bold yellow]Shrimp Posture Detected![/bold yellow]\n")
    console.print("1. Sit up straight.")
    console.print("2. Roll your shoulders back.")
    console.print("3. Unclench your jaw.")
    console.print("4. Blink.\n")
    console.print("[green]Good human.[/green]\n")

def window():
    console.print("\n[bold cyan]🪟 Opening the blinds...[/bold cyan]\n")
    try:
        # wttr.in with ?0 (current weather only), q (quiet)
        headers = {"User-Agent": "curl/7.68.0"} # curl user-agent forces terminal output format
        response = requests.get("https://wttr.in/?0q", headers=headers, timeout=5)
        if response.status_code == 200:
            # wttr.in outputs ANSI, rich prints it exactly as-is if we print without markup if needed, 
            # but rich handles most basic ANSI fine, or we can just print directly.
            print(response.text)
        else:
            console.print("It's cloudy. Or the API is down. Just look out a real window!")
    except:
        console.print("[red]Could not reach the outside world. Please look through a physical window.[/red]\n")

def mirror():
    compliments = [
        "Your Git commit messages are surprisingly descriptive.",
        "You're doing great. Even senior devs have to Google how to center a div.",
        "Your code is beautiful and so are you.",
        "You are capable of resolving those merge conflicts.",
        "I'm just a terminal, but I think you're awesome.",
        "Your logic is sound and your variables are well-named.",
        "That bug wasn't your fault. Probably.",
        "You make the digital world a better place."
    ]
    console.print("\n[bold cyan]🪞 *Looking in the mirror*[/bold cyan]\n")
    console.print(f"[bold magenta]{random.choice(compliments)}[/bold magenta]\n")

def hydrate():
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    state = {"date": None, "glasses": 0}
    if os.path.exists(WATER_STATE_FILE):
        try:
            with open(WATER_STATE_FILE, 'r') as f:
                state = json.load(f)
        except:
            pass
            
    if state["date"] != today_str:
        state["date"] = today_str
        state["glasses"] = 0
        
    state["glasses"] += 1
    
    with open(WATER_STATE_FILE, 'w') as f:
        json.dump(state, f)
        
    glasses = state["glasses"]
    
    console.print("\n[bold blue]💧 Hydration Tracker[/bold blue]\n")
    
    level = min(glasses, 8)
    empty_space = 8 - level
    
    bottle = "   ___\n"
    bottle += "  |   |\n"
    bottle += "  |___|\n"
    for i in range(empty_space):
        bottle += "  |   |\n"
    for i in range(level):
        bottle += "  |~~~|\n"
    bottle += "  '---'\n"
    
    console.print(f"[cyan]{bottle}[/cyan]")
    
    console.print(f"Glasses today: [bold]{glasses}[/bold] / 8")
    if glasses >= 8:
        console.print("[bold green]Hydration goal reached! Excellent work.[/bold green]\n")
    else:
        console.print("[yellow]Keep drinking! Stay hydrated, human.[/yellow]\n")
