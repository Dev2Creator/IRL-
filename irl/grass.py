import os
import json
from datetime import datetime, timedelta
from irl.state import add_coins

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
    from irl.themes import get_engine
    engine = get_engine()
    
    state = load_state()
    today_str = datetime.now().strftime("%Y-%m-%d")
    today_date = datetime.strptime(today_str, "%Y-%m-%d").date()
    
    if state["last_touched"] == today_str:
        engine.ui.render_generic("⚠️ Grass already touched today. Come back tomorrow.")
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
    
    engine.render_grass()
    add_coins(50, "Touched grass")
    
    rank = get_rank(state["streak"])
    days_text = "day" if state["streak"] == 1 else "days"
    engine.ui.render_generic(f"Current Streak: {state['streak']} {days_text}\nRank: {rank}\n")
