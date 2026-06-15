import os
import json

STATE_FILE = os.path.expanduser("~/.irl_state.json")

def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, 'r') as f:
                state = json.load(f)
                # Migration for old state format
                if "active_banner" not in state:
                    state["active_banner"] = state.get("active_theme", "default")
                    state["active_tone"] = state.get("active_theme", "default")
                    state["active_color"] = state.get("active_theme", "default")
                    state["purchased_banners"] = state.get("purchased_themes", ["default"])
                    state["purchased_tones"] = state.get("purchased_themes", ["default"])
                    state["purchased_colors"] = state.get("purchased_themes", ["default"])
                return state
        except:
            pass
    return {
        "coins": 0,
        "active_banner": "default",
        "active_tone": "default",
        "active_color": "default",
        "purchased_banners": ["default"],
        "purchased_tones": ["default"],
        "purchased_colors": ["default"]
    }

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)

def add_coins(amount, message=""):
    state = load_state()
    state["coins"] += amount
    save_state(state)
    
    if message:
        try:
            from irl.themes import get_engine
            engine = get_engine()
            engine.render_coin_gain(amount, message)
        except Exception:
            from rich.console import Console
            Console().print(f"\n[yellow]🪙  +{amount} IRL Coins[/yellow] [dim]({message})[/dim]")
        
    return state["coins"]
