<div align="center">

# IRL™ 🌱

### Software for humans. Useful tools. Less terminal drama.

A warm, keyboard-driven command center for installing packages, inspecting registries, diagnosing setup problems, and remembering that developers require water and sunlight.

[![PyPI](https://img.shields.io/pypi/v/irl-pkg?style=flat-square&color=E47C55&label=PyPI)](https://pypi.org/project/irl-pkg/)
[![Python](https://img.shields.io/pypi/pyversions/irl-pkg?style=flat-square&color=D7C0AA)](https://pypi.org/project/irl-pkg/)
[![License](https://img.shields.io/github/license/Dev2Creator/IRL-?style=flat-square&color=614B39)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Dev2Creator/IRL-?style=flat-square&color=3478F6)](https://github.com/Dev2Creator/IRL-/stargazers)

[Install](#install) · [Explore](#what-is-inside) · [Commands](#commands) · [Routing](#one-command-several-sources) · [Rollback](#the-moai-rollback-ritual)

</div>

---

    ██╗ ██████╗  ██╗
    ██║ ██╔══██╗ ██║        IRL™
    ██║ ██████╔╝ ██║        ─────────────
    ██║ ██╔══██╗ ██║        Find the useful thing.
    ██║ ██║  ██║ ███████╗   Let the terminal handle it.
    ╚═╝ ╚═╝  ╚═╝ ╚══════╝

IRL turns a terminal window into a human-friendly software toolbox. Ask it to install a package, inspect what a registry knows, check whether your machine is ready, or step away from the screen for thirty seconds.

## Install

    pip install --upgrade irl-pkg

Then open the interactive command board:

    irl

Or go directly to a command:

    irl glasses requests
    irl doctor chalk
    irl install octocat/Hello-World

## What is inside

| Path | What you get |
|---|---|
| Universal install | Routes names, GitHub repositories, and direct URLs |
| Glasses | Package version, size, source, and install method |
| Doctor | Network, storage, package-source, and tool checks |
| Package search | Natural-language discovery for useful packages |
| Dashboard | The full keyboard-driven IRL command board |
| Store and games | Local progression, themes, and playable tools |
| IRL City | Terminal economy and story-like exploration |
| Manga and story | Reading, downloads, and branching terminal play |
| Wellness | Grass streaks, posture, hydration, weather, and compliments |
| Moai rituals | Safe delayed upgrades and version rollback |

The interface uses Rich panels, command palettes, warm burnt-orange accents, persistent local progress, and the same human-first visual language as IRL Wisdom.

## Commands

Core package tools:

    irl install <package-or-url>
    irl glasses <package>
    irl doctor <package>
    irl search <natural-language-query>
    irl run <command>

Human maintenance:

    irl grass
    irl posture
    irl hydrate
    irl window
    irl mirror
    irl chaos

The wider command center:

    irl dashboard
    irl store
    irl games
    irl city
    irl manga
    irl story
    irl bones
    irl joke
    irl dog

Package maintenance:

    irl upgrade
    irl rollback

Run `irl --help` for the current command list and command-specific options.

## One command, several sources

IRL chooses a route from the target you give it:

| Input | Route |
|---|---|
| `requests` | Checks PyPI, then npm, then GitHub search |
| `chalk` | Installs from npm when the package exists there |
| `owner/repository` | Downloads the repository's default archive |
| `https://.../archive.zip` | Downloads and extracts a direct archive |
| `https://.../script.py` | Downloads the direct file |

Examples:

    irl install requests
    irl install chalk
    irl install octocat/Hello-World
    irl install https://example.com/tool.zip

Review third-party code before running it. IRL simplifies routing; it does not certify the safety of packages or repositories.

## The Moai upgrade ritual

On Windows, a running launcher can lock its own executable. IRL hands the upgrade to a delayed helper so the current process can exit first:

    irl upgrade

The helper runs:

    python -m pip install --upgrade irl-pkg

## The Moai rollback ritual

Choose from available PyPI releases:

    irl rollback

Or request a known version directly:

    irl rollback 1.7.5 --yes

Manual pinning remains available:

    pip index versions irl-pkg
    pip install --upgrade irl-pkg==1.7.5

Rollback changes the installed package version. Local IRL state remains on your machine.

## Local state

IRL stores its own progression locally:

    ~/.irl_state.json
    ~/.irl_grass.json

When the optional shared IRL identity package is installed, IRL can also greet the profile stored at:

    ~/.irl/profile.json

No IRL account is required for the core package tools.

## How it works

    irl
    ├── argparse command routing
    ├── Rich terminal rendering
    ├── PyPI and npm registry checks
    ├── GitHub repository lookup
    ├── direct download and extraction
    ├── local progression and themes
    └── delayed pip maintenance helpers

## Development

    git clone https://github.com/Dev2Creator/IRL-.git
    cd IRL-
    python -m pip install -e .
    irl

Build a release:

    python -m build

## Author

Created by **Anika Mukherjee**

Email: [cuteypieanika@gmail.com](mailto:cuteypieanika@gmail.com)

GitHub: [@Dev2Creator](https://github.com/Dev2Creator)

## Copyright, trademark, and license

Copyright © 2026 Anika Mukherjee. All rights reserved.

**IRL™** is a trademark of Anika Mukherjee.

The source code is licensed under the [GNU Affero General Public License v3 or later](LICENSE).

---

<div align="center">

Built for humans who use terminals, not terminals pretending humans do not exist. 🗿

</div>
