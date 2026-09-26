<div align="center">

# IRL™ 🌱

### Software for humans. Useful tools. Less terminal drama.

A warm, keyboard-driven command center for installing packages, inspecting registries, diagnosing setup problems, and remembering that developers require water and sunlight. Now with a garden roguelike, a rhythm game, and a pet.

[![PyPI](https://img.shields.io/pypi/v/irl-pkg?style=flat-square&color=E47C55&label=PyPI)](https://pypi.org/project/irl-pkg/)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/irl-pkg?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/irl-pkg)
[![Python](https://img.shields.io/pypi/pyversions/irl-pkg?style=flat-square&color=D7C0AA)](https://pypi.org/project/irl-pkg/)
[![License](https://img.shields.io/github/license/Dev2Creator/IRL-?style=flat-square&color=614B39)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Dev2Creator/IRL-?style=flat-square&color=3478F6)](https://github.com/Dev2Creator/IRL-/stargazers)
[![CI](https://img.shields.io/badge/CI-Actions-2088FF?style=flat-square)](https://github.com/Dev2Creator/IRL-/actions)

[Install](#install) · [Commands](#commands) · [Routing](#one-command-several-sources) · [Rollback](#the-moai-rollback-ritual)

</div>

---

## Install

```bash
pip install --upgrade irl-pkg
```

Then run:

```bash
irl
```

First launch walks you through a short onboarding: a splash, a name, a vibe picker with live previews, and a 30-second tour. Works on **Linux, macOS, and Windows** — same commands, same chaos, zero crashes.

## What is inside

| | |
|---|---|
| 📦 **Universal installer** | PyPI, npm, GitHub, or a direct URL — `irl install` figures out the registry. |
| 🩺 **Doctor & glasses** | Diagnose your setup; inspect a package before trusting it. |
| 🌱 **Grass streak** | Touch grass daily. Ranks, XP, and a GitHub-style contribution heatmap. |
| 🎮 **Games** | Classics plus **Grassland Quest** (garden roguelike) and **Lofi Rhythm** (beat game) — free. |
| 🐾 **IRL Pet** | A terminal tamagotchi that evolves with your streak and sulks when skipped. |
| 🏆 **Achievements & quests** | Daily quests pay coins; coins buy themes, games, and personality. |
| 🏪 **18 themes** | Synthwave, Sakura, Terminal Classic, High-Contrast... and one you have to find. |
| 🎵 **71 lofi loops** | Bundled. Play cross-platform via winsound/aplay/ffplay/afplay/paplay. |
| 🌈 **Full-screen TUI** | `irl tui` — an optional Textual app (`pip install 'irl-pkg[tui]'`). |

## Commands

### The useful part

| Command | What it does |
|---|---|
| `irl install <pkg>` | Installs from PyPI, npm, GitHub (`owner/repo`), or a direct URL. |
| `irl glasses <pkg>` | Version, size, and source of any package, before you commit. |
| `irl doctor <pkg>` | Checks network, storage, and toolchain before installs go sideways. |
| `irl search <query>` | AI-assisted package search that ends in an install offer. |
| `irl run <cmd>` | Runs a command; in a project folder it quietly becomes `npm run <cmd>`. |
| `irl upgrade` | Upgrades IRL™ itself. |
| `irl rollback [ver]` | Time-travels irl-pkg to any published version. Interactive picker; `--yes` for the impatient. |
| `irl lang` | The bundled `.irl` toy language: `run <file>`, `demo`, or `repl`. |

### The wellness part

| Command | What it does |
|---|---|
| `irl grass` | Touch grass. Daily. The streak is guarded by your pet and your conscience. |
| `irl hydrate` / `irl posture` / `irl window` / `irl mirror` / `irl chaos` | Small rituals with strong opinions about your spine. |
| `irl quests` | Three daily quests that pay coins. |
| `irl achievements` | Trophies and your level: Noob → Code Gremlin → 10x Dev → Grass Sensei. |
| `irl pet` | Adopt a duck, cat, dog, or plant. It earns coins. It remembers neglect. |

### The fun part

| Command | What it does |
|---|---|
| `irl dashboard` | Mission control: real stats, grass heatmap, tips, everything one keypress away. |
| `irl games` | Tic-Tac-Toe, RPS, Chess & Ludo sims — plus Grassland Quest (G) and Lofi Rhythm (R), free. |
| `irl grassland` | Garden-maze roguelike: collect water and sunshine, dodge literal bugs, defeat The Deadline. Winning extends your streak. |
| `irl rhythm` | 4-lane falling-note beat game (D/F/J/K) charted from the bundled lofi loops. |
| `irl city` | IRL City: jobs, car theft, bank robberies, a wanted level. |
| `irl store` | Buy themes, spare parts, and games with coins. Live previews included. |
| `irl story` | Themed branching stories. One of them is about MS-DOS. |
| `irl bones` / `irl joke` / `irl dog` / `irl manga` | Lofi beats, developer jokes, ASCII dogs, manga. |
| `irl tui` | Full-screen Textual app: home, installer, games, and a lofi player. |

### The secret part

Some things aren't in the help. Codes open doors. That is all we say.

## One command, several sources

```bash
irl install requests                      # PyPI
irl install express                       # npm
irl install owner/repo                    # GitHub (branch resolved via the API)
irl install https://example.com/pkg.zip   # direct URL
```

Detection order: direct URL → GitHub `owner/repo` → PyPI → npm → GitHub keyword search. Archives are extracted into a **named directory** with a preview of what lands on disk, and path-traversal tricks ("zip-slip") are blocked and reported.

## The Moai upgrade ritual

```bash
irl upgrade
```

Upgrade entrusts the stone to a delayed pip process, so your current command exits cleanly on every OS.

## The Moai rollback ritual

```bash
irl rollback             # interactive version picker
irl rollback 1.7.5 --yes # direct, no confirmations, for the brave
```

Versions come straight from PyPI; the downgrade runs detached so your terminal stays yours.

## Local state

Everything lives in your home folder: `~/.irl_state.json` (profile, coins, themes), `~/.irl_grass.json` (streak + heatmap), `~/.irl_pet.json` (your pet), `~/.irl_quests.json` (daily board), `~/.irl_rhythm.json` (high scores), `~/.irl_achievements.json` (trophies). Delete them to start over; your pet will remember, briefly.

## Audio

Bundled lofi loops play via winsound (Windows), aplay, ffplay, afplay, or paplay — whatever your system has. No audio backend? IRL™ degrades to air guitar, gracefully.

## Development

```bash
git clone https://github.com/Dev2Creator/IRL- IRL-
cd IRL-
pip install -e '.[dev,tui]'
ruff check .
pytest
python -m build
```

CI runs ruff + pytest + build on Ubuntu, macOS, and Windows across Python 3.9–3.13. See [CONTRIBUTING.md](CONTRIBUTING.md) and [CHANGELOG.md](CHANGELOG.md).

## Author

**Anika Mukherjee** — [Dev2Creator](https://github.com/Dev2Creator)

## Copyright, trademark & license

IRL™ is a trademark of Anika Mukherjee. All rights reserved regarding the mark.

Copyright © 2026 Anika Mukherjee. This program is free software: you can redistribute it and/or modify it under the terms of the **GNU Affero General Public License v3 or later** — see [LICENSE](LICENSE).

*In loving memory of the bundled GTA 1997 zip (2024–2026). It has ridden into the sunset for licensing-karma reasons. Touch real grass instead.*
