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

"""The full-screen IRL™ TUI (optional ``irl-pkg[tui]`` extra).

Home tab: pet, streak and quests. Tabs for the installer, games and the
lofi player. Built with Textual; if it is missing we print a friendly
nudge instead of a traceback.
"""

import json
import os
import subprocess
import sys

from rich.panel import Panel

from irl.console import console
from irl.ui import IRL_ACCENT, IRL_BORDER, IRL_MUTED

try:
    from textual.app import App, ComposeResult
    from textual.containers import Horizontal
    from textual.widgets import Footer, Header, Input, ListItem, ListView, Static, TabbedContent, TabPane

    HAS_TEXTUAL = True
except ImportError:  # the [tui] extra is optional
    HAS_TEXTUAL = False

PET_FILE = os.path.expanduser("~/.irl_pet.json")
GRASS_FILE = os.path.expanduser("~/.irl_grass.json")
QUESTS_FILE = os.path.expanduser("~/.irl_quests.json")

_FALLBACK_PET = r"""
      __
  ___( o )>
  \ <_. )
   `---'   no pet yet — run `irl pet` to adopt one
"""


def _read_json(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def run_tui():
    if not HAS_TEXTUAL:
        console.print(
            Panel(
                "[bold]The full-screen TUI needs the Textual engine.[/bold]\n\n"
                "[#D7C0AA]Install it with one command:[/#D7C0AA]\n"
                f"[bold {IRL_ACCENT}]    pip install 'irl-pkg[tui]'[/{IRL_ACCENT}]\n\n"
                f"[dim]{IRL_MUTED}Until then, `irl dashboard` remains your trusty command board.[/dim]",
                title="[bold #F29265]IRL TUI[/bold #F29265]",
                border_style=IRL_BORDER,
            )
        )
        return

    IRLTui().run()


if HAS_TEXTUAL:

    class IRLTui(App):
        TITLE = "IRL™ 2.0"
        SUB_TITLE = "Software for Humans. Less terminal drama."
        CSS = """
        Screen { background: $surface; }
        #home { padding: 1 2; }
        #petbox { width: 1fr; }
        #statsbox { width: 1fr; }
        Static.title { color: $accent; text-style: bold; margin-bottom: 1; }
        ListView { height: 1fr; }
        Input { margin-bottom: 1; }
        #output { height: 1fr; border: round #6B4E36; padding: 0 1; }
        """

        BINDINGS = [("q", "quit", "Quit"), ("d", "toggle_dark", "Toggle dark")]

        def compose(self) -> ComposeResult:
            yield Header(show_clock=True)
            with TabbedContent(initial="home"):
                with TabPane("🏠 Home", id="home"):
                    yield Horizontal(
                        Static(self._pet_panel(), id="petbox"),
                        Static(self._stats_panel(), id="statsbox"),
                    )
                with TabPane("📦 Installer", id="installer"):
                    yield Static("[bold]Install anything: PyPI, npm, GitHub owner/repo, or a URL.[/bold]", classes="title")
                    yield Input(placeholder="package name, owner/repo, or https://...")
                    yield Static("<output>", id="output")
                with TabPane("🎮 Games", id="games"):
                    yield Static(self._games_panel())
                with TabPane("🎵 Lofi", id="music"):
                    yield ListView(*[ListItem(Static(os.path.basename(p))) for p in self._lofi_tracks()], id="tracks")
            yield Footer()

        # --- Home helpers ---------------------------------------------------

        def _pet_panel(self) -> str:
            pet = _read_json(PET_FILE, None)
            art = pet.get("art", _FALLBACK_PET) if pet else _FALLBACK_PET
            mood = pet.get("mood", "unhatched") if pet else "n/a"
            return Panel(f"{art}\n[bold]mood:[/] {mood}", title="pet", border_style=IRL_BORDER)

        def _stats_panel(self) -> str:
            grass = _read_json(GRASS_FILE, {})
            quests = _read_json(QUESTS_FILE, {})
            state = _read_json(os.path.expanduser("~/.irl_state.json"), {})
            lines = [
                f"[bold]operator:[/] {state.get('name', 'human')}",
                f"[bold]coins:[/] {state.get('coins', 0)}",
                f"[bold]grass streak:[/] {grass.get('streak', 0)} days",
                "",
                "[bold #F29265]today's quests[/bold #F29265]",
            ]
            for quest in quests.get("today", []):
                mark = "x" if quest.get("done") else " "
                lines.append(f"[{mark}] {quest.get('label', '?')}")
            if not quests.get("today"):
                lines.append("(run `irl quests` to generate)")
            return Panel("\n".join(lines), title="status", border_style=IRL_BORDER)

        def _games_panel(self) -> str:
            from irl.games import GAMES

            lines = ["Games run in their own full-screen mode:", ""]
            for _key, game in GAMES.items():
                lines.append(f"  [bold #F29265]{game['name']}[/bold #F29265] — [dim]{game['desc']}[/dim]")
            lines += ["", "Press q and run `irl games` to play them properly."]
            return Panel("\n".join(lines), title="game shelf", border_style=IRL_BORDER)

        @staticmethod
        def _lofi_tracks():
            from irl.audio import list_lofi

            return list_lofi()

        # --- Installer ------------------------------------------------------

        def on_input_submitted(self, event: Input.Submitted) -> None:
            target = event.value.strip()
            if not target:
                return
            output = self.query_one("#output", Static)
            output.update(f"installing [bold]{target}[/bold] ... grass being touched")
            self.run_worker(self._install_worker(target), exclusive=True)

        async def _install_worker(self, target: str) -> None:
            try:
                result = subprocess.run(
                    [sys.executable, "-m", "irl.main", "install", target],
                    capture_output=True,
                    text=True,
                    timeout=300,
                )
                text = (result.stdout or "") + (result.stderr or "")
            except Exception as exc:
                text = f"install exploded: {exc}"
            self.query_one("#output", Static).update(text.strip() or "(no output)")

        def on_list_view_selected(self, event: ListView.Selected) -> None:
            node = event.item.children[0] if event.item.children else None
            if node is None:
                return
            track = str(node.renderable)
            from irl.audio import list_lofi, play_track

            for path in list_lofi():
                if os.path.basename(path) == track:
                    play_track(path)
                    self.query_one("#tracks", ListView).border_title = f"now playing: {track}"
                    break
