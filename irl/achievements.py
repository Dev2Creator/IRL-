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

"""Achievements + XP → levels.

Every IRL feature reports its milestones here via :func:`award` /
:func:`check_auto`. Unlocks persist in the main state file, so they
survive reinstalls of your dignity. Coins → XP → levels:
Noob → Code Gremlin → 10x Dev → Grass Sensei.
"""

import json
import os
from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from irl.state import add_coins, load_state, save_state

console = Console()

ACHIEVEMENTS_FILE = os.path.expanduser("~/.irl_achievements.json")

# id: (title, description, coin reward)
ACHIEVEMENTS = {
    "first_install": ("First Install", "Installed something with irl. The journey begins.", 20),
    "first_grass": ("Toucher of Grass", "Touched grass once. The sun said hi.", 20),
    "streak_7": ("7-Day Grass Streak", "One full week of going outside. Suspiciously healthy.", 100),
    "streak_30": ("30-Day Grass Streak", "A month outdoors. Your rank is showing.", 300),
    "bug_squasher": ("Bug Squasher", "Beat The Deadline in Grassland Quest.", 150),
    "rhythm_2000": ("Certified Groover", "Scored 2000+ in Lofi Rhythm.", 100),
    "night_owl": ("Night Owl", "Used IRL between 1 and 4 AM. The bugs saw you.", 30),
    "pet_parent": ("Pet Parent", "Adopted a terminal pet. Responsibility unlocked.", 50),
    "collector": ("Fashionista", "Owned 5 themes at once.", 200),
    "quest_master": ("Quest Master", "Completed all 3 daily quests in one day.", 120),
    "installer_10": ("Serial Installer", "Installed 10 things. node_modules fears you.", 80),
    "rich_kid": ("Coin Enjoyer", "Held 1000 coins at once.", 100),
}

# XP thresholds for levels.
LEVELS = [
    (0, "Noob", "everyone starts somewhere"),
    (300, "Code Gremlin", "you have discovered snacks in the build cache"),
    (1500, "10x Dev", "allegedly. the benchmarks are pending"),
    (5000, "Grass Sensei", "the lawn whispers your name"),
]


def load_unlocked():
    try:
        with open(ACHIEVEMENTS_FILE, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_unlocked(data):
    with open(ACHIEVEMENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f)


def _xp_of(state):
    """XP = total_xp (lifetime). Coins are spendable; XP is forever."""
    return state.get("total_xp", 0)


def get_level(state):
    xp = _xp_of(state)
    current = LEVELS[0]
    for threshold, name, tagline in LEVELS:
        if xp >= threshold:
            current = (threshold, name, tagline)
    return current


def award(achievement_id, quiet=False):
    """Unlock an achievement (idempotent) and pay out its coins."""
    if achievement_id not in ACHIEVEMENTS:
        return False
    unlocked = load_unlocked()
    if achievement_id in unlocked:
        return False
    title, desc, reward = ACHIEVEMENTS[achievement_id]
    unlocked[achievement_id] = datetime.now().strftime("%Y-%m-%d %H:%M")
    save_unlocked(unlocked)
    add_coins(reward, f"Achievement: {title}")
    state = load_state()
    state["total_xp"] = state.get("total_xp", 0) + 50
    save_state(state)
    if not quiet:
        console.print(
            Panel(
                f"[bold yellow]🏆 ACHIEVEMENT UNLOCKED[/bold yellow]\n\n[bold]{title}[/bold] — [dim]{desc}[/dim]\nReward: [bold]+{reward} coins[/bold], +50 XP",
                border_style="yellow",
            )
        )
    return True


def check_auto(context=None):
    """Milestones that can be derived from state alone. Call after any action.

    context: optional dict with hints like {'game': 'grassland_win'}.
    """
    state = load_state()
    hour = datetime.now().hour
    if hour in (1, 2, 3, 4):
        award("night_owl", quiet=True)
    try:
        with open(os.path.expanduser("~/.irl_grass.json"), encoding="utf-8") as f:
            grass = json.load(f)
        streak = grass.get("streak", 0)
        if grass.get("last_touched"):
            award("first_grass", quiet=True)
        if streak >= 7:
            award("streak_7", quiet=True)
        if streak >= 30:
            award("streak_30", quiet=True)
    except Exception:
        pass
    owned = len(state.get("purchased_colors", []))
    if owned >= 5:
        award("collector", quiet=True)
    if state.get("coins", 0) >= 1000:
        award("rich_kid", quiet=True)
    context = context or {}
    if context.get("game") == "grassland_win":
        award("bug_squasher", quiet=True)
    if context.get("game") == "rhythm_score" and context.get("score", 0) >= 2000:
        award("rhythm_2000", quiet=True)
    if context.get("pet_adopted"):
        award("pet_parent", quiet=True)
    if context.get("quests_all_done"):
        award("quest_master", quiet=True)
    if context.get("installed"):
        installs = load_unlocked().get("_install_count", 0) + 1
        data = load_unlocked()
        data["_install_count"] = installs
        save_unlocked(data)
        award("first_install", quiet=True)
        if installs >= 10:
            award("installer_10", quiet=True)


def show_achievements():
    state = load_state()
    unlocked = load_unlocked()
    _, level_name, level_tagline = get_level(state)
    xp = _xp_of(state)

    table = Table(show_header=True, expand=True)
    table.add_column("Achievement", style="bold")
    table.add_column("Description")
    table.add_column("Status", justify="right")
    for achievement_id, (title, desc, _reward) in ACHIEVEMENTS.items():
        if achievement_id in unlocked:
            status = f"[green]✔ {unlocked[achievement_id][:10]}[/green]"
        else:
            status = "[dim]locked[/dim]"
        table.add_row(title, desc, status)

    console.print(
        Panel(
            f"[bold]Level: {level_name}[/bold] — [dim]{level_tagline}[/dim]\nTotal XP: {xp}\nUnlocked: {len([a for a in ACHIEVEMENTS if a in unlocked])}/{len(ACHIEVEMENTS)}",
            title="🏆 Achievements",
            border_style="yellow",
        )
    )
    console.print(table)
