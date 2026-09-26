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

"""Cross-platform single-key input for interactive IRL features.

Windows uses msvcrt, POSIX uses termios+tty. Every keypress is normalized
into a :class:`Key` so callers never touch raw escape bytes again:

    from irl.keys import Key, read_key, flush_keys, is_interactive

    key = read_key()
    if key == Key.DOWN: ...
    elif key.is_char("q"): ...

Named keys: UP DOWN LEFT RIGHT ENTER ESC SPACE TAB BACKSPACE
CTRL_C CTRL_D EOF CHAR UNKNOWN.
"""

import os
import sys

_POSIX = os.name != "nt"

# Sentinel names for non-character keys.
UP, DOWN, LEFT, RIGHT = "UP", "DOWN", "LEFT", "RIGHT"
ENTER, ESC, SPACE, TAB, BACKSPACE = "ENTER", "ESC", "SPACE", "TAB", "BACKSPACE"
CTRL_C, CTRL_D, EOF, CHAR, UNKNOWN = "CTRL_C", "CTRL_D", "EOF", "CHAR", "UNKNOWN"

_ARROW_MAP_NT = {"H": UP, "P": DOWN, "K": LEFT, "M": RIGHT}
_ARROW_MAP_POSIX = {b"A": UP, b"B": DOWN, b"C": LEFT, b"D": RIGHT}


class Key:
    """One normalized keypress. ``name`` is a module constant, ``char`` the
    literal character for CHAR keys (None otherwise)."""

    __slots__ = ("name", "char")

    def __init__(self, name, char=None):
        self.name = name
        self.char = char

    def is_char(self, ch=None):
        if self.name != CHAR:
            return False
        return ch is None or self.char == ch

    def __eq__(self, other):
        if isinstance(other, Key):
            return self.name == other.name and self.char == other.char
        if isinstance(other, str):
            return self.name == other
        return NotImplemented

    def __hash__(self):
        return hash((self.name, self.char))

    def __repr__(self):
        if self.name == CHAR:
            return f"Key(CHAR, {self.char!r})"
        return f"Key({self.name})"


# Frequently used singletons (immutable in spirit; go ahead, try anyway).
KEY_UP = Key(UP)
KEY_DOWN = Key(DOWN)
KEY_LEFT = Key(LEFT)
KEY_RIGHT = Key(RIGHT)
KEY_ENTER = Key(ENTER)
KEY_ESC = Key(ESC)
KEY_SPACE = Key(SPACE)
KEY_TAB = Key(TAB)
KEY_BACKSPACE = Key(BACKSPACE)
KEY_CTRL_C = Key(CTRL_C)
KEY_CTRL_D = Key(CTRL_D)
KEY_EOF = Key(EOF)
KEY_UNKNOWN = Key(UNKNOWN)


def _named(name):
    return {
        UP: KEY_UP,
        DOWN: KEY_DOWN,
        LEFT: KEY_LEFT,
        RIGHT: KEY_RIGHT,
        ENTER: KEY_ENTER,
        ESC: KEY_ESC,
        SPACE: KEY_SPACE,
        TAB: KEY_TAB,
        BACKSPACE: KEY_BACKSPACE,
        CTRL_C: KEY_CTRL_C,
        CTRL_D: KEY_CTRL_D,
        EOF: KEY_EOF,
        UNKNOWN: KEY_UNKNOWN,
    }[name]


def is_interactive():
    """True when stdin is a real terminal the user types into."""
    try:
        return sys.stdin is not None and sys.stdin.isatty()
    except (AttributeError, ValueError):
        return False


def _select_byte(timeout):
    """Read one byte if it arrives within ``timeout`` seconds; else None (POSIX)."""
    import select

    ready, _, _ = select.select([sys.stdin], [], [], timeout)
    if not ready:
        return None
    return sys.stdin.read(1)


def _read_byte():
    """One raw byte/char from stdin; '' on EOF."""
    if _POSIX:
        return sys.stdin.read(1)
    import msvcrt

    return msvcrt.getwch()


def read_key():
    """Blocking read of one keypress, normalized. Raises EOFError on EOF."""
    if not is_interactive():
        raise EOFError("stdin is not a terminal; single-key input unavailable")

    if _POSIX:
        import termios
        import tty

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return _normalize_posix(ch)
    return _normalize_windows(_read_byte())


def _normalize_posix(ch):
    if ch == "":
        return KEY_EOF
    if ch == "\x1b":
        # Escape sequence? Peek briefly for the CSI bytes.
        nxt = _select_byte(0.05)
        if nxt == "[":
            code = _select_byte(0.05)
            name = _ARROW_MAP_POSIX.get(code.encode()) if code else None
            return _named(name) if name else KEY_UNKNOWN
        return KEY_ESC
    if ch in ("\r", "\n"):
        return KEY_ENTER
    if ch == "\x03":
        return KEY_CTRL_C
    if ch == "\x04":
        return KEY_CTRL_D
    if ch in ("\x7f", "\x08"):
        return KEY_BACKSPACE
    if ch == "\t":
        return KEY_TAB
    if ch == " ":
        return KEY_SPACE
    if 0x20 <= ord(ch) <= 0x10FFFF:
        return Key(CHAR, ch)
    return KEY_UNKNOWN


def _normalize_windows(ch):
    if ch in ("\x00", "\xe0"):
        arrow = msvcrt_getwch()
        return _named(_ARROW_MAP_NT.get(arrow, UNKNOWN))
    if ch == "\r":
        return KEY_ENTER
    if ch == "\x03":
        return KEY_CTRL_C
    if ch == "\x1b":
        return KEY_ESC
    if ch == "\x08":
        return KEY_BACKSPACE
    if ch == "\t":
        return KEY_TAB
    if ch == " ":
        return KEY_SPACE
    if ch.isprintable():
        return Key(CHAR, ch)
    return KEY_UNKNOWN


def msvcrt_getwch():
    import msvcrt

    return msvcrt.getwch()


def read_char(default=None):
    """Blocking single character, lowercased — for wasd-style game loops.

    Ctrl-C still raises KeyboardInterrupt so games stay polite.
    Returns ``default`` on EOF / non-interactive stdin.
    """
    try:
        key = read_key()
    except EOFError:
        return default
    if key == KEY_CTRL_C or key == KEY_CTRL_D:
        raise KeyboardInterrupt
    if key.is_char():
        return key.char.lower()
    if key == KEY_ENTER:
        return "\n"
    return default


def kbhit():
    """True if a keypress is waiting (never blocks)."""
    if not is_interactive():
        return False
    if _POSIX:
        return _select_byte(0) is not None
    import msvcrt

    return msvcrt.kbhit()


def flush_keys():
    """Discard pending keypresses (e.g. the Enter that launched us)."""
    if _POSIX:
        try:
            import termios

            termios.tcflush(sys.stdin.fileno(), termios.TCIFLUSH)
        except Exception:
            pass
        return
    try:
        import msvcrt

        while msvcrt.kbhit():
            msvcrt.getwch()
    except Exception:
        pass
