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

import argparse
import sys
from irl.install import install_package
from irl.glasses import inspect_package
from irl.doctor import run_doctor

def cli():
    banner = """
 [bold green]╔══════════════════════╗[/bold green]
 [bold green]║[/bold green]      [bold white]IRL™ 🌱[/bold white]         [bold green]║[/bold green]
 [bold green]║[/bold green] [bold cyan]Software for Humans[/bold cyan]  [bold green]║[/bold green]
 [bold green]╚══════════════════════╝[/bold green]"""
    
    from rich.console import Console
    Console().print(banner)
    
    parser = argparse.ArgumentParser(
        prog="irl",
        description="IRL (In Real Life) - Software for Humans."
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    install_parser = subparsers.add_parser("install", help="Get Started")
    install_parser.add_argument("package", help="Name of the package, GitHub repo, or direct URL")
    
    glasses_parser = subparsers.add_parser("glasses", help="See Clearly")
    glasses_parser.add_argument("package", help="Name of the package to inspect")
    
    doctor_parser = subparsers.add_parser("doctor", help="Stay Healthy")
    doctor_parser.add_argument("package", help="Name of the package to diagnose")
    
    grass_parser = subparsers.add_parser("grass", help="Go Outside")
    
    args = parser.parse_args()
    
    if args.command == "install":
        if not args.package:
            print("Error: Please provide a package name to install.")
            sys.exit(1)
        install_package(args.package)
    elif args.command == "glasses":
        if not args.package:
            print("Error: Please provide a package name to inspect.")
            sys.exit(1)
        inspect_package(args.package)
    elif args.command == "doctor":
        if not args.package:
            print("Error: Please provide a package name to diagnose.")
            sys.exit(1)
        run_doctor(args.package)
    elif args.command == "grass":
        from irl.grass import touch_grass
        touch_grass()
    else:
        menu = """
 [bold cyan]👓 Glasses[/bold cyan] - See Clearly
 [bold red]🩺 Doctor[/bold red]  - Stay Healthy
 [bold yellow]📦 Install[/bold yellow] - Get Started
 [bold green]🌱 Grass[/bold green]   - Go Outside
 
 Usage: irl <command> <package>
 
 [dim]© 2026 UNKNOWN™[/dim]
 """
        Console().print(menu)

if __name__ == "__main__":
    cli()
