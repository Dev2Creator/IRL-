# Changelog

All notable changes to irl-pkg are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and versions
follow [SemVer](https://semver.org/), mostly.

## [2.1.0] — The .irl Language: Full Platform

### Added — the language itself
- **The .irl language 2.1, professional edition** — Python's words with
  C's braces: `var`/`let`, `function`/`def`/`fn`, `if`/`elif`/`else`,
  `while`, `for (x in iterable)`, `break`/`continue`, `return`,
  `true`/`false`/`none`. Every legacy slang keyword still runs as an
  alias (zero breakage); the 2.0 `💦` print prefix is retired.
- **Optional semicolons** — newline ends a statement; `;` still legal.
- **Floats, string escapes, f-strings** (`f"hi {name + 1}"`), **dicts**
  (`keys()`/`values()`), list **slicing** and negative indexing.
- **Full builtin set** — `print` (multi-arg, `sep=`/`end=`), `input`,
  `int`, `float`, `str`, `len`, `range`, `sum`, `min`, `max`, `abs`,
  `round`, `sorted`, `type` (prints Python-exact `<class 'int'>`),
  `isinstance`, `append`.
- **Methods on values** — `s.upper()`, `s.split(",")`, `n.append(x)`,
  `d.keys()` and friends.
- **`memo function`** — automatic memoization, interpreter and compiler.
- **Imports** — stdlib capability allowlist (`math`, `random`, `time`,
  `datetime`, `json`, `string`, `statistics`) plus local modules:
  `import "utils.irl"`.
- **Professional errors** — line + column with caret rendering.

### Added — compiler & native core
- **`irl lang build`** — a real multi-pass compiler: constant folding,
  dead-code elimination, memo lowering, builtin caching at `-O2`;
  `-O0/-O1/-O2` levels, `--emit-py`/`--emit-ir` inspection, `-v` report,
  incremental `.irl_cache/`. Output: readable `.py` + executable `.pyc`.
  Benchmarks: **70–225× faster than interpreted, at CPython parity**.
- **`irl lang check --json`** and **`irl lang spec --json`** — CI/CD- and
  AI-friendly machine-readable validation and grammar.
- **`irl lang bench`** — honest published numbers, three engines.
- **Native accelerator core** (`native/_irl_native.c`) — the first
  non-.py engine component: the lexer as compiled machine code
  (clang/gcc → `_irl_native`), parity-proven token-for-token against the
  reference lexer, pure-Python fallback when absent. Platform wheels via
  the new cibuildwheel workflow.
- **Direct script running** — `irl myprogram.irl` works like
  `python file.py`; `#!/usr/bin/env irl` shebangs supported.

### Added — notebook & ecosystem
- **`irl notebook`** — Jupyter-style cell notebook for .irl: code +
  markdown cells, Shift+Enter execution, one persistent kernel, save/
  load `.irlnb`, export to `.irl`. Zero dependencies, localhost-only.
- **VS Code extension 1.2** — new logo icon, Run/Build commands with
  keybindings, error problem-matcher, 19 snippets covering the 2.1
  surface, f-string-aware grammar.
- **Brand** — original SVG logo (terminal `{ 🌱 }`), dark/light/mono
  variants.
- **Docs** — LANG.md (frozen spec), DESIGN.md (architecture law: Python
  is the bootstrap, SEESEMBLY IR contract, Zig native path, 2030
  roadmap), COMPILER.md, NOTEBOOK.md, AI_GUIDE.md.

## [2.0.0] — The Glow-Up Update

### Added
- **Grassland Quest** — a seeded garden-maze roguelike: collect water and
  sunshine, dodge literal bugs, boss-fight The Deadline. Winning extends
  your grass streak. Free, on the games menu (G).
- **Lofi Rhythm** — a 4-lane falling-note beat game (D/F/J/K) charted
  deterministically from the 71 bundled lofi loops, with combos and
  per-track high scores.
- **IRL Pet** — adopt a rubber duck, cat, dog, or plant. Evolves with
  care and streaks, sulks when skipped, earns coins back.
- **Achievements & XP levels** — 12 unlocks (First Install, 7-Day Grass
  Streak, Bug Squasher, Night Owl...) and levels Noob → Code Gremlin →
  10x Dev → Grass Sensei.
- **Daily quests** — three date-seeded quests per day feeding the coin
  economy.
- **`irl lang`** — the `.irl` toy language now ships with the package:
  `run <file>`, `demo`, and a persistent-environment `repl`.
- **`irl tui`** — full-screen Textual app (home / installer / games /
  lofi player) behind the `irl-pkg[tui]` extra.
- **`irl/ui.py` design system** — gradient wordmark banners, brand
  panels/tables/spinners, Nerd Font icons with automatic ASCII fallback,
  and styled error panels with actionable hints.
- **Animated first-run onboarding** — splash, name prompt, theme picker
  with live previews, and a 30-second tour.
- **Dashboard 2.0** — real system stats (pip/npm counts, disk), a
  GitHub-style grass contribution heatmap, rotating tips, and a compact
  22-command menu.
- **Five new themes** — Synthwave, Sakura, Terminal Classic,
  High-Contrast, and Matrix (secret unlockable), all with live store
  previews and full story-mode support.
- **Easter eggs** — konami code on the dashboard, `irl 42`, `irl pizza`.
  One of them opens a door.
- **Dev workflows** — ruff lint+format, pre-commit, GitHub Actions CI
  (3 OS × Python 3.9–3.13) with coverage gate, release workflow with
  PyPI trusted publishing, Dependabot, issue/PR templates,
  CONTRIBUTING.md, this CHANGELOG.
- **Test suite** — installer routing, zip-slip rejection, .irl language,
  grass/pet/quest/achievement logic, maze generation, rhythm scoring,
  and CLI smoke tests.

### Changed
- **Wheel size: 13.4 MB → ~1 MB.** The bundled GTA 1997 DOS game
  (12.4 MB) has been retired for licensing-karma reasons. The `g` key in
  IRL City now observes a moment of silence.
- **Cross-platform input** — `irl/keys.py` normalizes keyboard input
  (msvcrt on Windows, termios+tty on POSIX); the dashboard now works on
  Linux and macOS and degrades gracefully when piped.
- **Cross-platform audio** — `irl/audio.py` auto-detects winsound, aplay,
  ffplay, afplay, or paplay; bones no longer requires Windows or
  `C:\Temp`.
- **`irl rollback` implemented for real** — interactive questionary
  picker, `--yes` flag, and a delayed detached pip helper that is safe
  on every OS.
- **Security hardening** — all `shell=True` subprocess calls replaced
  with argument lists; archives extract into a named target directory
  after a preview, with per-member zip-slip validation and symlink
  rejection; download filenames sanitized.
- **Packaging** — author and license properly credited (Anika Mukherjee,
  AGPL-3.0-or-later), full classifiers, project URLs, `requires-python
  >=3.8`, `[tui]`/`[dev]` extras, and a `__version__` export.
- **README 2.0** — matches reality.

### Fixed
- Dashboard crashed on startup on Linux/macOS (bare `msvcrt` import).
- `irl run` passed a list to `shell=True`, executing only the first word.
- `run_doctor`'s shell-injection surface when checking tool versions.
- dog.py crashed at import time when Pillow was missing (now shows an
  ASCII dog).
- Hardcoded `C:\Users\aneek\...` path in generate_quiz.py.
- Story mode ignored your theme (stale `active_theme` key).

## [1.7.6] — 2026-06-26

- Onboarding polish: WISDOM OS header, identity/profile line, custom
  `--help`, and the Moai rollback ritual UI.
- Delayed-pip upgrade and rollback helpers.

## [1.7.0] — 2026-06-26

- Themes engine split into layouts/tones/engine; dashboard skins.
- IRL City economy mode with jobs, crime, and street races.

## [1.6.x] — 2026-06-20

- Store economy (coins, themes, games), story mode, and state file
  migration.

## [1.3.x – 1.5.x] — 2026-06-15

- Manga reader with offline cache, Professor Bones lofi, dog & joke
  commands, quiz-based chaos mode, bundled lofi audio.

## [1.0.x – 1.2.0] — 2026-06-14

- First public releases: universal installer routing (PyPI/npm/GitHub/
  URL), glasses, doctor, grass, creative wellness commands, and the
  original dashboard.

[2.0.0]: https://github.com/Dev2Creator/IRL-/releases/tag/v2.0.0
