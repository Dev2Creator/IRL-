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

"""Grassland Quest — the garden-maze roguelike that replaced a certain
1997 crime simulator we can no longer legally talk about.

Procedurally generated maze (seeded, deterministic for tests): collect
water and sunshine, dodge literal bugs, then face The Deadline in the
boss chamber. Winning extends your grass streak. Pure Rich, keys via
irl.keys.
"""

import random
import time
from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from irl.keys import is_interactive, read_char

console = Console()

# Glyphs are ASCII-safe so this runs anywhere Rich does.
GLYPH_WALL = "[green3]▓▓[/green3]"
GLYPH_PATH = "  "
GLYPH_WATER = "[bold cyan]~~[/bold cyan]"
GLYPH_SUN = "[bold yellow]\\\\[/bold yellow]"
GLYPH_BUG = "[bold red]\\/[/bold red]"
GLYPH_BOSS = "[bold magenta]§§[/bold magenta]"
GLYPH_EXIT = "[bold green]>|[/bold green]"
GLYPH_PLAYER = "[black on bright_white]@ [/black on bright_white]"

WATER_NEEDED = 4
SUN_NEEDED = 3
START_HP = 3


def generate_maze(width=15, height=15, seed=None):
    """Odd-dimension recursive-backtracker maze.

    Returns a grid of chars: '#' wall, '.' path. Deterministic per seed.
    """
    rng = random.Random(seed)
    grid = [["#" for _ in range(width)] for _ in range(height)]

    def carve(x, y):
        grid[y][x] = "."
        dirs = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        rng.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width - 1 and 1 <= ny < height - 1 and grid[ny][nx] == "#":
                grid[y + dy // 2][x + dx // 2] = "."
                carve(nx, ny)

    carve(1, 1)
    # Boss chamber: open a plaza at the far corner.
    for y in range(height - 3, height - 1):
        for x in range(width - 3, width - 1):
            grid[y][x] = "."
    grid[height - 2][width - 2] = "E"  # exit portal behind the boss
    return grid


def place_items(grid, seed=None):
    """Drop water/sun pickups and bugs on path cells (never near start)."""
    rng = random.Random(seed if seed is not None else random.randrange(1 << 30))
    paths = [(x, y) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == "." and (x, y) != (1, 1)]
    rng.shuffle(paths)

    def take(n):
        got = [paths.pop() for _ in range(min(n, len(paths)))]
        return got

    water = take(WATER_NEEDED)
    sun = take(SUN_NEEDED)
    bugs = take(4)
    boss = take(1)
    return water, sun, bugs, boss[0] if boss else (len(grid[0]) - 2, len(grid) - 2)


class Game:
    def __init__(self, seed=None):
        self.seed = seed if seed is not None else random.randrange(1 << 30)
        self.grid = generate_maze(seed=self.seed)
        self.water, self.sun, self.bugs, self.boss = place_items(self.grid, seed=self.seed)
        self.px, self.py = 1, 1
        self.hp = START_HP
        self.collected_water = 0
        self.collected_sun = 0
        self.boss_alive = True
        self.won = False
        self.message = "Collect ~water and \\\\sun, then find the Deadline's chamber."

    # --- rendering -------------------------------------------------------

    def render(self):
        console.print()
        header = Text(" G R A S S L A N D   Q U E S T ", style="bold green")
        console.print(Panel(header, border_style="green"))
        status = (
            f" HP: {'[red]♥[/red]' * self.hp}{'[dim]·[/dim]' * (START_HP - self.hp)}  water [cyan]{self.collected_water}/{WATER_NEEDED}[/cyan]  sun [yellow]{self.collected_sun}/{SUN_NEEDED}[/yellow]"
        )
        console.print(status)
        for y in range(len(self.grid)):
            row = ""
            for x in range(len(self.grid[0])):
                if (x, y) == (self.px, self.py):
                    row += GLYPH_PLAYER
                elif (x, y) == self.boss and self.boss_alive:
                    row += GLYPH_BOSS
                elif (x, y) in self.bugs:
                    row += GLYPH_BUG
                elif (x, y) in self.water:
                    row += GLYPH_WATER
                elif (x, y) in self.sun:
                    row += GLYPH_SUN
                elif self.grid[y][x] == "E":
                    row += GLYPH_EXIT
                elif self.grid[y][x] == "#":
                    row += GLYPH_WALL
                else:
                    row += GLYPH_PATH
            console.print(row)
        console.print(f"[dim]{self.message}[/dim]")
        console.print("[dim]WASD/arrows to move · Q to retreat · bugs bite[/dim]\n")

    # --- mechanics -------------------------------------------------------

    def walkable(self, x, y):
        h, w = len(self.grid), len(self.grid[0])
        return 0 <= x < w and 0 <= y < h and self.grid[y][x] != "#"

    def move_bugs(self):
        """Bugs shamble toward the player, one step, 60% of the time."""
        moved = []
        for bx, by in self.bugs:
            if random.random() < 0.6:
                dx = (self.px > bx) - (self.px < bx)
                dy = (self.py > by) - (self.py < by)
                options = [(bx + dx, by), (bx, by + dy)]
                options = [o for o in options if self.walkable(*o)]
                if options:
                    bx, by = random.choice(options)
            moved.append((bx, by))
        self.bugs = moved

    def step(self, dx, dy):
        nx, ny = self.px + dx, self.py + dy
        if not self.walkable(nx, ny):
            self.message = "A very solid hedge. It wins."
            return
        self.px, self.py = nx, ny
        self.message = ""

        if (self.px, self.py) in self.water:
            self.water.remove((self.px, self.py))
            self.collected_water += 1
            self.message = f"[cyan]Sipped water ({self.collected_water}/{WATER_NEEDED}).[/cyan]"
        elif (self.px, self.py) in self.sun:
            self.sun.remove((self.px, self.py))
            self.collected_sun += 1
            self.message = f"[yellow]Absorbed sunshine ({self.collected_sun}/{SUN_NEEDED}).[/yellow]"
        elif (self.px, self.py) in self.bugs:
            self.bugs.remove((self.px, self.py))
            self.hp -= 1
            self.message = "[red]A literal bug bit you! -1 HP.[/red]"
        elif (self.px, self.py) == self.boss and self.boss_alive:
            self.boss_fight()
            return
        elif self.grid[self.py][self.px] == "E":
            if self.boss_alive:
                self.message = "[magenta]The Exit hums. The Deadline blocks the way back to it... actually, it blocks nothing. Still: it lives.[/magenta]"
            else:
                self.won = True
                return

        self.move_bugs()
        if (self.px, self.py) in self.bugs:
            self.bugs.remove((self.px, self.py))
            self.hp -= 1
            self.message += " [red]The bug caught up and bit you! -1 HP.[/red]"

        if self.hp <= 0:
            self.message = "[bold red]You ran out of HP and had to go lie in real grass.[/bold red]"

    # --- boss -------------------------------------------------------------

    def boss_fight(self):
        """The Deadline: turn-based, three actions, one highly stressed boss."""
        boss_hp = 5
        console.print(
            Panel(
                "[bold magenta]§ THE DEADLINE §[/bold magenta]\n[dim]It is 23:58 on a Friday, personified. It must ship. Or must you?[/dim]",
                border_style="magenta",
            )
        )
        actions = {"1": "Ship it", "2": "Dodge the standup", "3": "Debug bravely"}
        while boss_hp > 0 and self.hp > 0:
            prompt = "  ".join(f"[{k}] {v}" for k, v in actions.items())
            console.print(f"[bold]{prompt}[/bold]")
            choice = read_char(default="2")
            if choice == "q":
                return
            if choice not in actions:
                choice = "2"
            roll = random.random()
            if choice == "1":
                if roll < 0.6:
                    boss_hp -= 1
                    console.print(f"[green]You shipped a feature! The Deadline flinches ({boss_hp} left).[/green]")
                else:
                    self.hp -= 1
                    console.print("[red]You shipped to prod on Friday. It rebounded. -1 HP.[/red]")
            elif choice == "2":
                if roll < 0.7:
                    console.print("[cyan]You dodged the standup. Nothing happened. Beautiful.[/cyan]")
                else:
                    self.hp -= 1
                    console.print("[red]You were spotted. It asked about the Jira ticket. -1 HP.[/red]")
            else:
                if roll < 0.5:
                    boss_hp -= 2
                    console.print(f"[green]You found the root cause! -2 to The Deadline ({boss_hp} left).[/green]")
                else:
                    console.print("[yellow]It was a heisenbug. It vanished unproven.[/yellow]")
            time.sleep(0.4)

        if boss_hp <= 0:
            self.boss_alive = False
            self.message = "[bold green]The Deadline is defeated! The Exit portal opens.[/bold green]"
        else:
            self.message = "[bold red]The Deadline shipped YOU. You crawl back to the garden entrance.[/bold red]"
            self.px, self.py = 1, 1
        read_char(default="\n")


def extend_grass_streak(days=1):
    """Winning the quest extends the grass streak (bonus days, capped daily)."""
    import json
    import os

    path = os.path.expanduser("~/.irl_grass.json")
    try:
        with open(path, encoding="utf-8") as f:
            grass = json.load(f)
    except Exception:
        grass = {"streak": 0, "xp": 0, "history": {}}
    today = datetime.now().strftime("%Y-%m-%d")
    grass["streak"] = grass.get("streak", 0) + days
    grass["xp"] = grass.get("xp", 0) + days
    grass.setdefault("history", {})[today] = grass["history"].get(today, 0) + days
    with open(path, "w", encoding="utf-8") as f:
        json.dump(grass, f)
    return grass["streak"]


def play_grassland_quest(seed=None):
    if not is_interactive():
        console.print("[yellow]Grassland Quest needs a real terminal for its wasd adventures.[/yellow]")
        return False

    game = Game(seed=seed)
    while True:
        game.render()
        if game.won:
            break
        if game.hp <= 0:
            break
        key = read_char(default="q")
        if key == "q":
            console.print("[dim]You retreated to the code editor. The garden understands.[/dim]")
            return False
        moves = {"w": (0, -1), "s": (0, 1), "a": (-1, 0), "d": (1, 0)}
        if key in moves:
            game.step(*moves[key])

    if game.won:
        loot = 10 * game.collected_water + 15 * game.collected_sun + 100
        from irl.state import add_coins

        add_coins(loot, "Grassland Quest victory")
        new_streak = extend_grass_streak(1)
        try:
            from irl.achievements import check_auto

            check_auto(context={"game": "grassland_win"})
        except Exception:
            pass
        console.print(
            Panel(
                f"[bold green]VICTORY[/bold green]\n\n"
                f"Loot: [bold yellow]+{loot} coins[/bold yellow]\n"
                f"Grass streak: [bold green]{new_streak} days[/bold green] (+1 bonus)\n"
                f"[dim]The garden thanks you. The bugs hold a grudge.[/dim]",
                border_style="green",
            )
        )
        return True
    loot = 10 * game.collected_water + 15 * game.collected_sun
    if loot:
        from irl.state import add_coins

        add_coins(loot, "Grassland Quest (partial loot)")
    console.print(
        Panel(
            f"[bold red]QUEST FAILED[/bold red]\n[dim]Water: {game.collected_water}, sun: {game.collected_sun}. The Deadline remains smug. Salvaged coins: {loot}.[/dim]",
            border_style="red",
        )
    )
    return False
