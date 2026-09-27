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

"""Regenerate the README screenshots (SVG) from real irl output.

Usage:  ~/.local/bin/irl-py scripts/make_screenshots.py
Writes: docs/shots/*.svg
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rich.console import Console

from irl.main import _build_dashboard
from irl.ui import wordmark

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "shots")
os.makedirs(OUT, exist_ok=True)


def save(console, name, title):
    console.save_svg(os.path.join(OUT, name), title=title)
    print(f"wrote {name}")


def shot_banner():
    c = Console(record=True, width=76, force_terminal=True, highlight=False)
    c.print(wordmark())
    c.print()
    c.print("[bold #F29265]irl --help[/bold #F29265]")
    c.print("[#D7C0AA]  install    Summon third-party code and hope it showers.[/#D7C0AA]")
    c.print("[#D7C0AA]  doctor     Diagnose your dependency swamp.[/#D7C0AA]")
    c.print("[#D7C0AA]  grass      Briefly cosplay as a mammal.[/#D7C0AA]")
    c.print("[#D7C0AA]  games      Grassland Quest · Lofi Rhythm · classics[/#D7C0AA]")
    c.print("[#D7C0AA]  pet        It evolves. It sulks. It pays rent in coins.[/#D7C0AA]")
    c.print("[dim]  …and 17 more. One command, every registry.[/dim]")
    save(c, "banner.svg", "irl — software for humans")


def shot_dashboard():
    from irl.state import load_state

    c = Console(record=True, width=112, height=44, force_terminal=True)
    c.print(_build_dashboard(load_state(), "Grass Touching Expert", "Anika", 3, 0))
    save(c, "dashboard.svg", "irl dashboard — command stone")


def shot_grassland():
    from irl.grassland_quest import GLYPH_BUG, GLYPH_PATH, GLYPH_PLAYER, GLYPH_SUN, GLYPH_WALL, GLYPH_WATER, SUN_NEEDED, WATER_NEEDED, Game

    c = Console(record=True, width=64, force_terminal=True)
    game = Game(seed=7)
    c.print()
    c.print("[bold green] G R A S S L A N D   Q U E S T [/bold green]")
    c.print(f" HP: [red]♥♥[/red]  water [cyan]2/{WATER_NEEDED}[/cyan]  sun [yellow]1/{SUN_NEEDED}[/yellow]")
    # deterministic hand-picked frame: draw the real maze, dress a few tiles
    for y in range(len(game.grid)):
        row = ""
        for x in range(len(game.grid[0])):
            if (x, y) == (game.px, game.py):
                row += GLYPH_PLAYER
            elif (x, y) == game.boss:
                row += "[bold magenta]§§[/bold magenta]"
            elif (x, y) in game.bugs:
                row += GLYPH_BUG
            elif (x, y) in game.water:
                row += GLYPH_WATER
            elif (x, y) in game.sun:
                row += GLYPH_SUN
            elif game.grid[y][x] == "E":
                row += "[bold green]>|[/bold green]"
            elif game.grid[y][x] == "#":
                row += GLYPH_WALL
            else:
                row += GLYPH_PATH
        c.print(row)
    c.print("[dim]WASD/arrows to move · Q to retreat · bugs bite[/dim]")
    save(c, "grassland.svg", "Grassland Quest")


def _hijack_console(module, recorder):
    """Point a module's rich output at our recording console."""
    module.console = recorder


def shot_pet():
    import irl.pet as pet_mod
    from irl.pet import render_pet

    c = Console(record=True, width=52, height=24, force_terminal=True)
    _hijack_console(pet_mod, c)
    c.print()
    pet = {
        "species": "duck",
        "name": "Quacktor",
        "adopted": "2026-08-01",
        "last_seen": "2026-09-27",
        "care": 31,
        "hunger": 0,
        "streak_seen": 42,
        "coins_earned": 233,
        "stage": "ascended",
    }
    render_pet(pet)
    save(c, "pet.svg", "irl pet")


def shot_store_preview():
    import irl.themes.layouts as layouts_mod
    from irl.ui import preview_theme

    c = Console(record=True, width=78, height=30, force_terminal=True)
    _hijack_console(layouts_mod, c)
    c.print()
    preview_theme("synthwave", console=c)
    save(c, "store-preview.svg", "IRL store — theme preview")


def shot_quests():
    import irl.quests as quests_mod
    from irl.quests import show_quests

    c = Console(record=True, width=82, height=26, force_terminal=True)
    _hijack_console(quests_mod, c)
    c.print()
    show_quests()
    save(c, "quests.svg", "daily quests")


if __name__ == "__main__":
    shot_banner()
    shot_dashboard()
    shot_grassland()
    shot_pet()
    shot_store_preview()
    shot_quests()
    print("done →", OUT)
