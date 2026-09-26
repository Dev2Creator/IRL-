# Contributing to IRL™ 🌱

Thanks for wanting to help build the wellness terminal. The rules are
few, the tone is warm, and the drama stays in the CI logs where it
belongs.

## Setup

```bash
git clone https://github.com/Dev2Creator/IRL- IRL-
cd IRL-
python -m venv .venv && source .venv/bin/activate   # or your usual ritual
pip install -e '.[dev,tui]'
pre-commit install
```

## Ground rules

1. **`ruff check .` must pass with zero violations.** `ruff format` is
   the arbiter of style arguments.
2. **Every feature ships with at least one test** covering its logic
   (state machines, scoring, routing — the parts that can break
   quietly).
3. **Cross-platform is non-negotiable.** If it uses msvcrt, winsound,
   or hard-coded paths, it's a bug. Use `irl.keys`, `irl.audio`, and
   `pathlib`.
4. **No shell=True.** Arg lists only; package names are user input.
5. **AGPL-3.0 headers stay** on all Python files, with the copyright
   line crediting Anika Mukherjee.
6. **No new heavy assets.** The wheel should stay under 2 MB. That is
   why GTA 1997 had to ride into the sunset.
7. Keep the brand voice: humorous, warm, never mean-spirited.

## Commit style

Conventional commits, subject in the imperative, humor welcome:

```
feat: teach the pet to hold grudges
fix: dashboard no longer assumes everyone owns a Windows keyboard
chore: ruff format, even the jokes
```

## Pull requests

Fill the template, keep PRs focused, and make sure CI is green.
Releases are cut by the maintainer via `scripts/release.sh` and
published with PyPI trusted publishing — contributors never need
credentials.

## Reporting bugs

Use the issue template and run the failing command with
`IRL_DEBUG=1` so we get the traceback.
