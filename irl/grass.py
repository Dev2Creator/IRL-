import os
import json
from datetime import datetime, timedelta
from rich.console import Console

console = Console()

STATE_FILE = os.path.expanduser("~/.irl_grass.json")

def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    return {"last_touched": None, "streak": 0, "xp": 0}

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)

def get_rank(streak):
    if streak >= 365:
        return "👑 Legendary Lawn Master"
    elif streak >= 180:
        return "🌍 Earth Guardian"
    elif streak >= 100:
        return "🌲 Forest Ranger"
    elif streak >= 60:
        return "🏞️ Outdoor Enthusiast"
    elif streak >= 30:
        return "🏅 Grass Veteran"
    elif streak >= 14:
        return "🌻 Sunlight Synthesizer"
    elif streak >= 7:
        return "🪴 Weekend Gardener"
    elif streak >= 3:
        return "🌱 Sprouting Nature Lover"
    else:
        return "🌿 Rookie Grass Toucher"

def touch_grass():
    state = load_state()
    today_str = datetime.now().strftime("%Y-%m-%d")
    today_date = datetime.strptime(today_str, "%Y-%m-%d").date()
    
    console.print("\n[bold green]🌱 Grass Touch Tracker[/bold green]\n")
    
    if state["last_touched"] == today_str:
        console.print("⚠️ Grass already touched today.\n")
        console.print("XP awarded: 0\n")
        console.print("Come back tomorrow.\n")
        return

    prev_streak = state["streak"]
    
    if state["last_touched"]:
        last_date = datetime.strptime(state["last_touched"], "%Y-%m-%d").date()
        if today_date - last_date == timedelta(days=1):
            state["streak"] += 1
        else:
            state["streak"] = 1
    else:
        state["streak"] = 1

    state["xp"] += 1
    state["last_touched"] = today_str
    save_state(state)
    
    if prev_streak == 0 or state["streak"] == 1:
        console.print("Current Streak: 0 days\n")
        console.print("Tip:\nGo outside.\nFind green object.\nTouch it.\n")
        console.print("Reward:\n+1 Grass XP\n")
        console.print("----------------------------------------\n")
        
    days_text = "day" if state["streak"] == 1 else "days"
    console.print(f"Current Streak: [bold]{state['streak']} {days_text}[/bold]\n")
    
    rank = get_rank(state["streak"])
    console.print(f"{rank}\n")
