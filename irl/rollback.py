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

"""``irl rollback`` — time travel, politely.

Lists published versions from PyPI, offers an interactive picker
(questionary when available, numbered table otherwise), and hands the
downgrade to a delayed pip process so the current command can exit
cleanly on every OS.
"""

import json
import os
import subprocess
import sys
import urllib.request

from rich import box
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

from irl.ui import IRL_ACCENT, IRL_CREAM, IRL_MUTED, IRL_BORDER

PACKAGE_NAME = "irl-pkg"
USER_AGENT = "IRL-Rollback/2.0"


def _version_tuple(value):
    try:
        return tuple(int(part) for part in str(value).split("."))
    except Exception:
        return (0,)


def pypi_versions(package_name=PACKAGE_NAME):
    request = urllib.request.Request(
        f"https://pypi.org/pypi/{package_name}/json",
        headers={"User-Agent": USER_AGENT},
    )
    with urllib.request.urlopen(request, timeout=10) as response:
        data = json.load(response)
    return sorted(data.get("releases", {}).keys(), key=_version_tuple, reverse=True)


def _launch_package_install(package_name, target_version):
    """Delayed, detached, shell-free pip install. Windows-safe."""
    pip_command = [
        sys.executable,
        "-m",
        "pip",
        "install",
        "--disable-pip-version-check",
        f"{package_name}=={target_version}",
    ]
    helper = (
        "import subprocess, sys, time; "
        "time.sleep(1.5); "
        "raise SystemExit(subprocess.call(sys.argv[1:]))"
    )
    creation_flags = getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
    subprocess.Popen([sys.executable, "-c", helper, *pip_command], creationflags=creation_flags)


def _pick_version(versions):
    """questionary picker with a numbered-table fallback."""
    try:
        import questionary
        shown = versions[:12]
        choices = [questionary.Choice(title=f"v{v}", value=v) for v in shown]
        choices.append(questionary.Choice(title="cancel — keep the current stone", value=None))
        return questionary.select(
            "Roll back to which version?",
            choices=choices,
        ).ask()
    except Exception:
        pass

    table = Table(show_header=False, box=None, expand=True, pad_edge=False)
    table.add_column("No", style=f"bold {IRL_MUTED}", no_wrap=True)
    table.add_column("Version", style=f"bold {IRL_ACCENT}", no_wrap=True)
    table.add_column("Action", style=IRL_CREAM)
    shown = versions[:12]
    aliases = {}
    for index, version_value in enumerate(shown, start=1):
        table.add_row(f"[{index}]", f"/{version_value:<12}", f"Install irl-pkg {version_value}")
        aliases[str(index)] = version_value
        aliases[version_value] = version_value
        aliases[f"/{version_value}"] = version_value
    table.add_row("[0]", "/cancel", "Leave the current stone in place")
    aliases["0"] = None
    aliases["cancel"] = None
    aliases["/cancel"] = None
    from rich.console import Console
    Console().print(table)
    raw_version = Prompt.ask(f"[{IRL_CREAM}]Version to install[/{IRL_CREAM}]", default="cancel").strip()
    return aliases.get(raw_version.lower(), raw_version.lstrip("/"))


def rollback_irl(target_version=None, yes=False):
    from rich.console import Console
    c = Console(highlight=False)
    package_name = PACKAGE_NAME

    if target_version is None and yes:
        c.print(f"[{IRL_CREAM}]--yes needs a version too: irl rollback 1.7.5 --yes[/{IRL_CREAM}]")
        return

    try:
        versions = pypi_versions(package_name)
    except Exception:
        c.print(f"[{IRL_CREAM}]The Moai cannot reach PyPI right now. Check your connection and try again.[/{IRL_CREAM}]")
        return

    if not versions:
        c.print(f"[{IRL_CREAM}]No old stones were found on PyPI.[/{IRL_CREAM}]")
        return

    if target_version is None:
        target_version = _pick_version(versions)

    if not target_version:
        c.print(f"[{IRL_MUTED}]Rollback cancelled. The stone stays still.[/{IRL_MUTED}]")
        return
    if target_version not in versions:
        c.print(f"[{IRL_CREAM}]Version {target_version} was not found for {package_name} on PyPI.[/{IRL_CREAM}]")
        return

    c.print(Panel(
        f"[{IRL_MUTED}]Package    [/{IRL_MUTED}][{IRL_CREAM}]{package_name}[/{IRL_CREAM}]\n"
        f"[{IRL_MUTED}]Target     [/{IRL_MUTED}][{IRL_ACCENT}]v{target_version}[/{IRL_ACCENT}]\n"
        f"[{IRL_MUTED}]Moai      [/{IRL_MUTED}][{IRL_ACCENT}]Rolling the stone backward.[/{IRL_ACCENT}]",
        title=f"[{IRL_ACCENT}]IRL Rollback Ritual[/{IRL_ACCENT}]",
        border_style=IRL_BORDER,
        box=box.SQUARE,
    ))

    if not yes:
        try:
            import questionary
            approved = questionary.confirm("Install this older IRL version?", default=True).ask()
        except Exception:
            approved = input("Install this older IRL version? [Y/n] ").strip().lower() not in ("n", "no")
        if not approved:
            c.print(f"[{IRL_MUTED}]Rollback cancelled. No files changed.[/{IRL_MUTED}]")
            return

    _launch_package_install(package_name, target_version)
    c.print(f"[{IRL_ACCENT}]🗿 Rollback started.[/{IRL_ACCENT}] [{IRL_CREAM}]pip will install {package_name}=={target_version} in a moment. "
            f"Run `irl --help` after it finishes to confirm.[/{IRL_CREAM}]")
