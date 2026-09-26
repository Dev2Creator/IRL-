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

class BaseLayout:
    def __init__(self, console):
        self.console = console

    def render_banner(self):
        self.console.print("--- IRL ---")

    def render_grass(self, text):
        self.console.print(text)

    def render_hydrate(self, text, glasses):
        self.console.print(text)

    def render_install(self, text):
        self.console.print(text)

    def render_coin_gain(self, amount, msg):
        self.console.print(f"🪙 +{amount} coins: {msg}")
        
    def render_generic(self, text):
        self.console.print(text)

    def render_node_modules(self, text):
        self.console.print(text)

    def render_run_start(self, text):
        self.console.print(text)

    def render_run_success(self, text):
        self.console.print(text)
