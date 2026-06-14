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

def chaos():
    import random
    import html as html_mod
    console.print("\n[bold magenta]🌪️  Summoning the Chaos Quiz...[/bold magenta]\n")
    
    quiz = None
    
    # --- Attempt 1: Open Trivia DB (free, reliable, no key needed) ---
    try:
        categories = [18, 9, 19, 15]  # Computers, General, Math, Video Games
        cat = random.choice(categories)
        url = f"https://opentdb.com/api.php?amount=1&category={cat}&type=multiple"
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            data = res.json()
            if data.get("response_code") == 0 and data.get("results"):
                result = data["results"][0]
                question = html_mod.unescape(result["question"])
                correct = html_mod.unescape(result["correct_answer"])
                incorrects = [html_mod.unescape(a) for a in result["incorrect_answers"]]
                
                options = incorrects + [correct]
                random.shuffle(options)
                correct_letter = ["a", "b", "c", "d"][options.index(correct)]
                
                quiz = {
                    "question": question,
                    "a": options[0],
                    "b": options[1],
                    "c": options[2],
                    "d": options[3],
                    "correct_key": correct_letter
                }
    except Exception:
        pass
    
    # --- Attempt 2: Pollinations AI (free, but rate-limited) ---
    if quiz is None:
        try:
            url = "https://text.pollinations.ai/openai"
            payload = {
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a chaotic Quiz Master. Generate a funny multiple-choice question for a software developer. Output ONLY valid JSON: {\"question\":\"...\",\"a\":\"...\",\"b\":\"...\",\"c\":\"...\",\"d\":\"...\",\"correct_key\":\"a or b or c or d\"}"
                    },
                    {"role": "user", "content": "Generate the chaotic dev quiz."}
                ],
                "jsonMode": True
            }
            response = requests.post(url, json=payload, timeout=15)
            if response.status_code == 200:
                data = response.json()
                content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
                content = content.replace("```json", "").replace("```", "").strip()
                quiz = json.loads(content)
        except Exception:
            pass
    
    # --- Attempt 3: Offline fallbacks (always works) ---
    if quiz is None:
        console.print("[dim](Drawing from the ancient chaotic archives...)[/dim]\n")
        try:
            from irl.quiz_bank import QUIZ_BANK
        except ImportError:
            from quiz_bank import QUIZ_BANK
        quiz = random.choice(QUIZ_BANK)
    
    # --- Display the quiz ---
    try:
        console.print(f"[bold yellow]❓ {quiz.get('question', 'What is happening?')}[/bold yellow]\n")
        console.print(f"  [cyan]A)[/cyan] {quiz.get('a', 'Error')}")
        console.print(f"  [cyan]B)[/cyan] {quiz.get('b', 'Error')}")
        console.print(f"  [cyan]C)[/cyan] {quiz.get('c', 'Error')}")
        console.print(f"  [cyan]D)[/cyan] {quiz.get('d', 'Error')}\n")
        
        user_ans = input("Choose your fate (A/B/C/D): ").strip().lower()
        correct = str(quiz.get('correct_key', '')).lower()
        
        if user_ans and user_ans == correct:
            console.print("\n[bold green]✅ You survived the chaos... for now.[/bold green]\n")
        else:
            console.print(f"\n[bold red]❌ INCORRECT! The chaos consumes you. The correct answer was {correct.upper()}.[/bold red]")
            console.print("[bold yellow]PUNISHMENT: Do 10 pushups immediately or drop all your production databases![/bold yellow]\n")
    except Exception as e:
        console.print(f"[red]The chaos escaped containment: {e}[/red]\n")

def chaos_counter():
    import colorsys
    from rich.text import Text
    console.print("\n[bold magenta]🎭 Entering the Chaos Counter...[/bold magenta]\n")
    
    try:
        url = "https://v2.jokeapi.dev/joke/Programming,Miscellaneous?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            joke_data = res.json()
            if not joke_data.get('error'):
                text = joke_data.get('joke', 'No joke found.')
            else:
                text = "Why did the API cross the road? To get rate limited."
        else:
            text = "Why did the API cross the road? To get rate limited."
    except:
        text = "Why did the programmer quit his job? Because he didn't get arrays."

    lines = text.split('\n')
    width = max(len(line) for line in lines)
    
    cow = []
    cow.append("  " + "_" * (width + 2))
    if len(lines) == 1:
        cow.append(f"< {lines[0]} >")
    else:
        cow.append(f"/ {lines[0].ljust(width)} \\")
        for line in lines[1:-1]:
            cow.append(f"| {line.ljust(width)} |")
        cow.append(f"\\ {lines[-1].ljust(width)} /")
    cow.append("  " + "-" * (width + 2))
    cow.append(r"        \   ^__^")
    cow.append(r"         \  (oo)\_______")
    cow.append(r"            (__)\       )\/\ ")
    cow.append(r"                ||----w |")
    cow.append(r"                ||     ||")
    
    rainbow_text = Text()
    for i, line in enumerate(cow):
        hue = (i / len(cow)) % 1.0
        rgb = colorsys.hls_to_rgb(hue, 0.6, 1.0)
        r, g, b = [int(x * 255) for x in rgb]
        color = f"#{r:02x}{g:02x}{b:02x}"
        rainbow_text.append(line + "\n", style=color)
        
    console.print(rainbow_text)
    console.print()
