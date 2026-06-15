import os
import glob

COPYRIGHT = """# IRL™ 🌱 - Software for Humans
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
"""

def add_copyright():
    py_files = glob.glob('irl/**/*.py', recursive=True) + ['generate_quiz.py']
    for fpath in py_files:
        if not os.path.exists(fpath): continue
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if "# IRL™ 🌱" not in content:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(COPYRIGHT + "\n" + content)
            print(f"Added copyright to {fpath}")

def update_tones():
    tones_path = "irl/themes/tones.py"
    with open(tones_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple replaces to make it personal
    content = content.replace("wage slave", "{name}")
    content = content.replace("human", "{name}")
    content = content.replace("Human", "{name}")
    content = content.replace("meatbag", "{name}")
    content = content.replace("snowflake", "{name}")
    
    with open(tones_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated tones to use {name}")

if __name__ == "__main__":
    add_copyright()
    update_tones()
