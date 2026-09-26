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

"""The IRL™ design system.

Every command renders through here: gradient wordmark banners, panels,
tables, spinners, icons with automatic ASCII fallback, and errors that
help instead of scream. Theming-aware — pull the active skin's colors
with :func:`accent`/:func:`border`.
"""

import os
import sys

from rich import box
from rich.console import Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

IRL_ACCENT = "#F29265"
IRL_CREAM = "#D7C0AA"
IRL_MUTED = "#614B39"
IRL_BORDER = "#6B4E36"

# --- Icons -----------------------------------------------------------------
# (nerd_font_glyph, ascii_fallback) — ascii is always safe to render.
ICONS = {
    "grass":      ("\uf06c", "[~]"),
    "water":      ("\uf773", "[W]"),
    "sun":        ("\uf185", "[*]"),
    "package":    ("\uf187", "[+]"),
    "search":     ("\uf002", "[?]"),
    "doctor":     ("\uf0f1", "[!]"),
    "glasses":    ("\uf570", "[o]"),
    "coin":       ("\uf3d1", "$"),
    "star":       ("\uf005", "*"),
    "heart":      ("\uf004", "<3"),
    "bug":        ("\uf188", "x"),
    "duck":       ("\ueb29", "<>"),
    "cat":        ("\uf6be", "=^.^="),
    "dog":        ("\uf6d3", "/\\_/\\"),
    "plant":      ("\uf4d8", "\\|/"),
    "game":       ("\uf11b", "[>]"),
    "music":      ("\uf001", "o/"),
    "trophy":     ("\uf091", "#1"),
    "fire":       ("\uf06d", "^"),
    "rocket":     ("\uf135", "/^\\"),
    "warning":    ("\uf071", "/!\\"),
    "check":      ("\uf00c", "OK"),
    "cross":      ("\uf00d", "X"),
    "arrow_right":("\uf061", "->"),
    "sparkles":   ("\uf890", "*"),
    "lock":       ("\uf023", "[L]"),
    "ghost":      ("\uf6e2", "BOO"),
    "skull":      ("\uf714", "X("),
}

# Terminals that advertise Nerd Font-capable rendering.
_NERD_HINT_ENV = (
    "KITTY_WINDOW_ID", "WEZTERM_EXECUTABLE", "ITERM_PROFILE",
    "WT_SESSION", "TERMINAL_EMULATOR", "ALACRITTY_LOG",
)


def icons_mode():
    """'nerd', 'ascii' or 'auto' — resolved from env, then state."""
    forced = os.environ.get("IRL_ICONS", "").strip().lower()
    if forced in ("nerd", "ascii", "auto"):
        return forced
    try:
        from irl.state import load_state
        mode = load_state().get("icons", "auto")
        return mode if mode in ("nerd", "ascii", "auto") else "auto"
    except Exception:
        return "auto"


def nerd_available():
    """Heuristic: does this terminal likely render Nerd Font glyphs?"""
    if not sys.stdout.isatty():
        return False
    if os.environ.get("CI"):
        return False
    if "256color" in os.environ.get("TERM", "") or os.environ.get("COLORTERM"):
        return any(var in os.environ for var in _NERD_HINT_ENV)
    return False


def use_nerd_icons():
    mode = icons_mode()
    return nerd_available() if mode == "auto" else mode == "nerd"


def icon(name):
    """Glyph for ``name``; ASCII fallback unless Nerd Fonts are on."""
    nerd, ascii_ = ICONS.get(name, ("", "?"))
    return nerd if (nerd and use_nerd_icons()) else ascii_


# --- Colors ----------------------------------------------------------------

def skin():
    """The active dashboard skin dict (accent/border/box/title/art)."""
    try:
        from irl.themes.layouts import DASHBOARD_SKINS
        from irl.themes import get_engine
        return DASHBOARD_SKINS.get(get_engine().color_id, DASHBOARD_SKINS["default"])
    except Exception:
        from irl.themes.layouts import DASHBOARD_SKINS
        return DASHBOARD_SKINS["default"]


def accent():
    return skin()["accent"]


def border():
    return skin()["border"]


# --- Banners ---------------------------------------------------------------

_WORDMARK = [
    ("██╗██████╗ ██╗     ", "#F29265"),
    ("██║██╔══██╗██║     ", "#F49B6A"),
    ("██║██████╔╝██║     ", "#F6A46F"),
    ("██║██╔══██╗██║     ", "#F8AD74"),
    ("██║██║  ██║███████╗", "#FBB679"),
    ("╚═╝╚═╝  ╚═╝╚══════╝", "#D7C0AA"),
]


def wordmark(subtitle=None, no_color=False):
    """The gradient IRL™ wordmark. Returns a renderable Group."""
    lines = Group(*[
        Text(line, style="bold " + (color if not no_color else "default"))
        for line, color in _WORDMARK
    ])
    tagline = subtitle or "Software for Humans. Useful tools. Less terminal drama."
    return Group(lines, Text(f"✦ {tagline} ✦", style=IRL_CREAM if not no_color else "default"))


def banner(console=None):
    """Print the full gradient banner."""
    from rich.console import Console
    (console or Console()).print(wordmark())
    (console or Console()).print()


# --- Panels / tables / spinners --------------------------------------------

def panel(body, title=None, **kwargs):
    """A brand-styled Panel."""
    return Panel(
        body,
        title=title,
        border_style=kwargs.pop("border_style", border()),
        box=kwargs.pop("box", box.SQUARE),
        **kwargs,
    )


def styled_table(title=None, **kwargs):
    """A Table pre-styled with brand colors."""
    table = Table(
        title=title,
        show_header=kwargs.pop("show_header", True),
        header_style=f"bold {accent()}",
        border_style=border(),
        box=kwargs.pop("box", box.SQUARE),
        **kwargs,
    )
    return table


def spinner(text):
    """console.status with brand flavor: `with ui.spinner("..."):`"""
    from irl.console import console
    return console._console.status(f"[{accent()}]{text}[/{accent()}]")


# --- Errors ----------------------------------------------------------------

def styled_error(message, hint=None, title="Well, this is awkward"):
    """Every failure becomes a styled panel with an actionable hint."""
    from irl.console import console
    lines = [Text(str(message), style="bold red")]
    if hint:
        lines.append(Text(""))
        lines.append(Text(f"Hint: {hint}", style=IRL_CREAM))
    lines.append(Text(""))
    lines.append(Text("Still stuck? Run `irl doctor` and describe the pain.", style=f"dim {IRL_MUTED}"))
    console.print(panel(Group(*lines), title=f"[bold red]{title}[/bold red]", border_style="red"))


def styled_success(message):
    from irl.console import console
    console.print(f"[bold {accent()}]{icon('check')} {message}[/{accent()}]")


# --- Theme preview -----------------------------------------------------------

def preview_theme(theme_id, console=None):
    """Render a live sample of a theme: banner line, panel, table row."""
    from rich.console import Console
    try:
        from irl.themes.layouts import LAYOUTS, DASHBOARD_SKINS
    except Exception:
        return
    console = console or Console()
    layout_cls = LAYOUTS.get(theme_id)
    skin_data = DASHBOARD_SKINS.get(theme_id, DASHBOARD_SKINS["default"])
    a, b = skin_data["accent"], skin_data["border"]

    console.print(Panel(
        Text(f"PREVIEW — {skin_data['title']}", style=f"bold {a}"),
        border_style=b, box=skin_data["box"],
    ))
    if layout_cls is not None:
        try:
            layout_cls().render_banner()
        except Exception:
            pass
    sample = Table(show_header=False, box=skin_data["box"], border_style=b, expand=True)
    sample.add_column(style=f"bold {a}")
    sample.add_column(style="white")
    sample.add_row("install", f"Installing your hopes via {theme_id}...")
    sample.add_row("grass", "Touched. It was real. It was soft.")
    console.print(sample)
    console.print()
