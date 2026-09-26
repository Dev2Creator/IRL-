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

"""IRL Pet — a terminal tamagotchi with a work ethic.

Species: rubber duck, cat, dog, or plant. Lives in ~/.irl_pet.json.
Evolves with your grass streak, earns coins when cared for, and sulks
openly when you skip days. It has seen your commit history. It still
loves you.
"""

import json
import os
import random
from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt

from irl.state import add_coins, load_state

console = Console()

PET_FILE = os.path.expanduser("~/.irl_pet.json")

SPECIES = {
    "duck": {"name": "Rubber Duck", "emoji": "🦆", "ascii": r"   __\n  <(o )___\n   ( ._> /\n    `---'"},
    "cat": {"name": "Terminal Cat", "emoji": "🐈", "ascii": r"  /\_/\ \n ( o.o )\n  > ^ <"},
    "dog": {"name": "Compile Dog", "emoji": "🐕", "ascii": r"  / \__\n (    @\___\n /         O\n/   (_____/\n/_____/   U"},
    "plant": {"name": "Office Fern", "emoji": "🪴", "ascii": r"   \\|/\n   .-.\n  (   )\n (_/ \_)"},
}

# Evolution stages by care level (visits + streaks). Names are load-bearing jokes.
STAGES = ["egg", "baby", "teen", "adult", "ascended"]
STAGE_TITLES = {
    "egg": "Egg of Potential",
    "baby": "Lil' Bugger",
    "teen": "Rebellious Process",
    "adult": "Fully Compiled Companion",
    "ascended": "Production-Ready Legend",
}

MOODS = {
    "happy": ["radiating joy", "purring at 60fps", "wagging through stdout", "photosynthesizing happily"],
    "sulk": ["judging your streak silently", "drawing a bath of disappointing beeps", "drooping, but politely"],
    "hungry": ["eyeing your snacks", "making the saddest syntax", "staring into your soul for treats"],
}


def load_pet():
    if os.path.exists(PET_FILE):
        try:
            with open(PET_FILE, encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return None


def save_pet(pet):
    with open(PET_FILE, "w", encoding="utf-8") as f:
        json.dump(pet, f)


def _days_since(iso_str):
    try:
        then = datetime.strptime(iso_str, "%Y-%m-%d").date()
        return (datetime.now().date() - then).days
    except Exception:
        return 0


def _care_level(pet):
    """Care score: feedings/plays + grass streak synergy."""
    return pet.get("care", 0) + min(pet.get("streak_seen", 0), 60) // 6


def _stage(pet):
    level = _care_level(pet)
    thresholds = [(0, "egg"), (3, "baby"), (8, "teen"), (16, "adult"), (30, "ascended")]
    stage = "egg"
    for threshold, name in thresholds:
        if level >= threshold:
            stage = name
    return stage


def _mood(pet):
    days = _days_since(pet.get("last_seen", datetime.now().strftime("%Y-%m-%d")))
    if days >= 2:
        return "sulk"
    if pet.get("hunger", 0) >= 3:
        return "hungry"
    return "happy"


def pet_art(pet):
    species = SPECIES.get(pet.get("species", "duck"), SPECIES["duck"])
    art = species["ascii"].replace("\\n", "\n")
    stage = pet.get("stage", "egg")
    if stage == "egg":
        art = "    .--.\n   ( .. )\n    '--'  (something stirs)"
    elif stage == "ascended":
        art += "\n ✨ " + "✨ " * 3
    return art


def adopt_pet():
    console.print("[bold cyan]Welcome to the IRL™ Pet Adoption Center.[/bold cyan]\n")
    console.print("A pet will watch you code. A pet will judge nothing. A pet will still be there.\n")
    options = list(SPECIES.keys())
    for idx, key in enumerate(options, start=1):
        console.print(f"  [bold]{idx}.[/bold] {SPECIES[key]['emoji']} {SPECIES[key]['name']}")
    choice = IntPrompt.ask("Who is coming home with you?", choices=[str(i) for i in range(1, len(options) + 1)], default=1)
    species = options[choice - 1]
    name = console.input(f"Name your {SPECIES[species]['name']}: ").strip() or "Duck Jr."
    pet = {
        "species": species,
        "name": name,
        "adopted": datetime.now().strftime("%Y-%m-%d"),
        "last_seen": datetime.now().strftime("%Y-%m-%d"),
        "care": 0,
        "hunger": 0,
        "streak_seen": 0,
        "coins_earned": 0,
    }
    _sync_pet(pet)
    save_pet(pet)
    console.print(f"\n[bold green]🎉 {name} the {SPECIES[species]['name']} joined your terminal![/bold green]")
    try:
        from irl.achievements import check_auto

        check_auto(context={"pet_adopted": True})
    except Exception:
        pass
    return pet


def _sync_pet(pet):
    """Evolution + mood housekeeping on every visit."""
    streak = 0
    try:
        with open(os.path.expanduser("~/.irl_grass.json"), encoding="utf-8") as f:
            streak = json.load(f).get("streak", 0)
    except Exception:
        pass
    pet["streak_seen"] = streak
    pet["stage"] = _stage(pet)
    today = datetime.now().strftime("%Y-%m-%d")
    if pet.get("last_seen") != today:
        pet["hunger"] = pet.get("hunger", 0) + 1
        pet["last_seen"] = today
    save_pet(pet)


def render_pet(pet):
    species = SPECIES.get(pet.get("species", "duck"), SPECIES["duck"])
    mood = _mood(pet)
    mood_text = random.choice(MOODS[mood])
    stage_title = STAGE_TITLES.get(pet.get("stage", "egg"), "Unknown Lifeform")
    art = pet_art(pet)
    info = (
        f"{species['emoji']} [bold]{pet.get('name', '???')}[/bold] — {stage_title}\n"
        f"mood: [italic]{mood_text}[/italic]\n"
        f"care: {pet.get('care', 0)}   hunger: {pet.get('hunger', 0)}   coins earned: {pet.get('coins_earned', 0)}"
    )
    if mood == "sulk":
        info += "\n[dim]They remember the days you didn't visit. Pets keep receipts.[/dim]"
    console.print(Panel(f"{art}\n\n{info}", title="🐾 IRL Pet", border_style="cyan"))


def feed_pet(pet):
    state = load_state()
    if state.get("coins", 0) < 10:
        console.print(f"[red]Feeding costs 10 coins. You have {state.get('coins', 0)}. Earn coins via games or quests.[/red]")
        return pet
    add_coins(-10, f"Feeding {pet.get('name', 'the pet')}")
    pet["hunger"] = max(0, pet.get("hunger", 0) - 2)
    pet["care"] = pet.get("care", 0) + 1
    _sync_pet(pet)
    earn = random.choice([5, 8, 10])
    add_coins(earn, f"{pet.get('name', 'Pet')} brought you a coin")
    pet["coins_earned"] = pet.get("coins_earned", 0) + earn
    save_pet(pet)
    console.print(f"[green]{pet.get('name')} ate. Hunger down, care up. They left you {earn} coins in gratitude.[/green]")
    return pet


def play_with_pet(pet):
    pet["care"] = pet.get("care", 0) + 1
    _sync_pet(pet)
    save_pet(pet)
    console.print(f"[green]You and {pet.get('name')} played 'chase the cursor'. Pure joy. (care +1)[/green]")
    return pet


def pet_cli():
    pet = load_pet()
    if pet is None:
        pet = adopt_pet()
        return
    _sync_pet(pet)
    try:
        from irl.quests import report as report_quest

        report_quest("pet")
    except Exception:
        pass
    while True:
        render_pet(pet)
        console.print("\n[bold]1.[/bold] Feed (10 coins)   [bold]2.[/bold] Play   [bold]0.[/bold] Back\n")
        choice = console.input("What shall we do? ").strip()
        if choice == "0":
            break
        elif choice == "1":
            pet = feed_pet(pet)
        elif choice == "2":
            pet = play_with_pet(pet)
