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
        "name": None,
        "coins": 0,
        "active_banner": "default",
        "active_tone": "default",
        "active_color": "default",
        "purchased_banners": ["default"],
        "purchased_tones": ["default"],
        "purchased_colors": ["default"],
        "total_xp": 0
    }

def get_global_rank(state):
    xp = state.get("total_xp", state.get("coins", 0))
    if xp >= 50000:
        return "Ascended Being"
    elif xp >= 10000:
        return "Terminal Overlord"
    elif xp >= 5000:
        return "Senior IRL Developer"
    elif xp >= 2500:
        return "Grass Touching Expert"
    elif xp >= 1000:
        return "Junior Developer"
    elif xp >= 500:
        return "Script Kiddie"
    else:
        return "Wage Slave"

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)

def add_coins(amount, message=""):
    state = load_state()
    state["coins"] += amount
    state["total_xp"] = state.get("total_xp", state.get("coins", 0)) + amount
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
