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

import re
from rich.console import Console

class IRLConsole:
    def __init__(self):
        self._console = Console()

    def _get_active_theme(self):
        # Import dynamically to avoid circular dependencies if state imports console
        from irl.state import load_state
        state = load_state()
        return state.get("active_theme", "default")

    def _apply_theme(self, text, theme):
        if not isinstance(text, str):
            return text
            
        if theme == "hacker":
            # Matrix green everywhere
            text = re.sub(r'\[/?(?:bold )?(?:red|blue|yellow|cyan|magenta|white|green)\]', '[bold green]', text)
            text = text.replace('[/bold green]', '[/]')
        elif theme == "cyberpunk":
            # Neon equivalents
            text = text.replace('red]', 'bright_magenta]').replace('blue]', 'bright_cyan]')\
                       .replace('yellow]', 'bright_yellow]').replace('cyan]', 'bright_cyan]')\
                       .replace('magenta]', 'bright_magenta]').replace('green]', 'bright_green]')
        elif theme == "dracula":
            # Dracula palette hex codes
            text = text.replace('red]', '#ff5555]').replace('blue]', '#bd93f9]')\
                       .replace('yellow]', '#f1fa8c]').replace('cyan]', '#8be9fd]')\
                       .replace('magenta]', '#ff79c6]').replace('green]', '#50fa7b]')\
                       .replace('white]', '#f8f8f2]')
        
        return text

    def print(self, *args, **kwargs):
        theme = self._get_active_theme()
        
        if theme == "default":
            self._console.print(*args, **kwargs)
            return

        new_args = []
        for arg in args:
            new_args.append(self._apply_theme(arg, theme))
            
        self._console.print(*new_args, **kwargs)

    def input(self, *args, **kwargs):
        theme = self._get_active_theme()
        
        if theme == "default":
            return self._console.input(*args, **kwargs)

        new_args = []
        for arg in args:
            new_args.append(self._apply_theme(arg, theme))
            
        return self._console.input(*new_args, **kwargs)

console = IRLConsole()
