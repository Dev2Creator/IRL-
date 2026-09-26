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

"""Daily quests — three rotating tasks a day feeding the coin economy.

Seeded by the date, so everyone gets the same set per day and the same
day always regenerates the same board (testable, deterministic). State
lives in ~/.irl_quests.json; progress is reported by the features
themselves via :func:`report`.
"""

import json
import os
import random
from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from irl.state import load_state, save_state, add_coins

console = Console()

QUESTS_FILE = os.path.expanduser("~/.irl_quests.json")

# quest id: (label, hint, coin reward)
QUEST_POOL = {
    "grass": ("Touch grass", "irl grass", 50),
    "install": ("Install a package", "irl install <pkg>", 30),
    "doctor": ("Run a checkup", "irl doctor system", 20),
    "hydrate": ("Log a glass of water", "irl hydrate", 15),
    "posture": ("Fix the shrimp posture", "irl posture", 15),
    "games": ("Play any game", "irl games", 25),
    "pet": ("Visit your pet", "irl pet", 15),
    "city": ("Visit IRL City", "irl city", 20),
    "glasses": ("Inspect a package", "irl glasses <pkg>", 20),
}


def load_board():
    try:
        with open(QUESTS_FILE, "r", encoding="utf-8") as f:
            board = json.load(f)
    except Exception:
        board = {}
    today = datetime.now().strftime("%Y-%m-%d")
    if board.get("date") != today:
        board = {"date": today, "today": generate_quests(today), "history": board.get("history", {})}
        save_board(board)
    return board


def save_board(board):
    with open(QUESTS_FILE, "w", encoding="utf-8") as f:
        json.dump(board, f)


def generate_quests(date_str):
    """Three deterministic quests per date (same day -> same board)."""
    rng = random.Random(f"irl-quests-{date_str}")
    picks = rng.sample(sorted(QUEST_POOL.keys()), 3)
    quests = []
    for qid in picks:
        label, hint, reward = QUEST_POOL[qid]
        quests.append({"id": qid, "label": label, "hint": hint, "reward": reward, "done": False})
    return quests


def report(quest_id, done=True):
    """Features call this when their quest-shaped action happens."""
    board = load_board()
    changed = False
    for quest in board["today"]:
        if quest["id"] == quest_id and not quest["done"] and done:
            quest["done"] = True
            add_coins(quest["reward"], f"Daily quest: {quest['label']}")
            changed = True
    if changed:
        save_board(board)
        if all(q["done"] for q in board["today"]):
            board.setdefault("history", {})[board["date"]] = True
            save_board(board)
            from irl.achievements import check_auto
            check_auto(context={"quests_all_done": True})
            console.print(Panel(
                "[bold green]ALL DAILY QUESTS COMPLETE[/bold green]\n"
                "[dim]The void has been held at bay for one more day.[/dim]",
                border_style="green",
            ))
    return changed


def show_quests():
    board = load_board()
    done = sum(1 for q in board["today"] if q["done"])
    console.print(Panel(
        f"[bold cyan]📋 DAILY QUESTS[/bold cyan] — [dim]{board['date']}[/dim]\n"
        f"Progress: {done}/3 — rewards pay out the moment a quest completes.",
        border_style="cyan",
    ))
    table = Table(show_header=True, expand=True)
    table.add_column("Quest", style="bold")
    table.add_column("Command", style="dim")
    table.add_column("Reward", justify="right", style="yellow")
    table.add_column("Status", justify="right")
    for quest in board["today"]:
        status = "[green]✔ done[/green]" if quest["done"] else "[red]pending[/red]"
        table.add_row(quest["label"], quest["hint"], f"+{quest['reward']}", status)
    console.print(table)
