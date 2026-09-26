# LAUNCH KIT — IRL™ 2.0.0 "The Glow-Up Update"

Everything here is a **draft for Anika to review and post herself**.
Nothing has been published. Dates, screenshots and numbers marked
`[TBD]` need filling in before posting.

Suggested order: Reddit (r/commandline first) → Show HN (weekday
morning US time) → Product Hunt (Tuesday–Thursday). Space them a few
days apart. Reply to every comment for the first 24h — that's what
makes or breaks these launches.

---

## 1. Show HN

**Title** (77 chars):

> Show HN: IRL – a gamified terminal command center (installer, games, lofi, pet)

**URL to submit**: https://github.com/Dev2Creator/IRL-

**First comment (post immediately as the maker):**

Hi HN — I'm Anika, sole maintainer of IRL (irl-pkg on PyPI). It
started as a joke of a wrapper around pip and grew into something I
use daily, so I rebuilt it properly and I'd love a technical
roast.

What it actually is:

- **Universal installer** — `irl install <anything>` sniffs the target:
  PyPI, npm, GitHub `owner/repo` (branch resolved via the API, not
  hardcoded), or a direct URL. Archives are extracted into a named
  directory with a preview, and every member is validated against path
  traversal before writing (zip-slip).
- **`irl doctor` / `irl glasses`** — preflight checks and package
  metadata before you install something regrettable.
- **`irl rollback`** — lists every published version from the PyPI JSON
  API and hands the downgrade to a detached `pip` child so your current
  process exits cleanly (works on Windows too).

The unusual part — it's deliberately gamified:

- A grass-streak tracker with a contribution heatmap on the dashboard
- Grassland Quest, a seeded garden-maze roguelike (pure Rich, ~400
  lines, boss fight included) that extends your streak when you win
- Lofi Rhythm, a 4-lane beat game charted deterministically from 71
  short WAV loops bundled in the wheel
- A terminal pet, daily quests, achievements, coins, and 18 themes —
  one of which is hidden

Engineering details I care about:

- Cross-platform by construction: one keyboard abstraction
  (msvcrt/termios+tty), one audio engine (winsound → aplay → ffplay →
  afplay → paplay). The whole thing runs on Linux, macOS, and Windows.
- The wheel is 976 KB. It shipped at 13.4 MB until I found a way to
  retire a bundled DOS game for licensing reasons.
- No `shell=True` anywhere; subprocess calls are arg lists.
- AGPL-3.0, Python 3.8+, zero-dependency-bloat (requests, rich,
  Pillow, questionary). CI on 3 OS × Python 3.9–3.13.

Known trade-offs I'm curious about feedback on: the gamification is
the point, but I know it won't be for everyone — there's a high
contrast theme and the games are strictly opt-in. And the dashboard is
Rich-based, not Textual (Textual is available as `irl-pkg[tui]`).

PyPI: https://pypi.org/project/irl-pkg/

---

## 2. Product Hunt kit

**Name**: IRL — Terminal Wellness OS

**Tagline** (58 chars):

> Install anything, touch grass, pet a duck — all in your terminal

**Description**:

IRL is a command center for your terminal that installs from PyPI,
npm, GitHub, or a URL with one command — and turns maintenance into a
game. Track a grass streak with a contribution heatmap, adopt a pet
that evolves with your habits, play a garden roguelike or a lofi
rhythm game, earn coins, buy themes. 976 KB, cross-platform, AGPL,
free forever.

**Maker comment**:

Hey PH 👋 I'm Anika. I built IRL because terminals are where I live
but nothing in them reminded me I'm a mammal. v2.0 is a full rebuild:
a universal installer that figures out the registry for you, real
system stats, a garden roguelike, a beat game made from 71 lofi loops,
and a pet that sulks if you skip days. Everything works on Linux,
macOS and Windows; the whole wheel is under 1 MB. It's AGPL open
source — roast it, fork it, install it, and go touch grass. 🌱

**Gallery captions**:
1. Banner: "IRL™ — the glow-up update"
2. Dashboard: "Real stats, grass heatmap, 22 commands, one keypress away"
3. Grassland Quest: "Dodge literal bugs. Defeat The Deadline."
4. Pet: "It evolves. It sulks. It pays rent in coins."
5. Install flow: "PyPI, npm, GitHub or URL — it just knows."

---

## 3. Reddit — r/commandline

**Title**: IRL: a cross-platform terminal command center — universal installer, doctor/glasses, rollback, plus a grass streak heatmap and a garden roguelike (AGPL, 976KB wheel)

**Body**:

Hey r/commandline. Long-time lurker, first tool I've shipped properly.

**irl** (pip install irl-pkg) is a command center that does a few
genuinely useful things and a few deliberately silly ones:

Useful:
- `irl install <pkg>` — routes between PyPI / npm / GitHub / direct URL
  automatically. GitHub `owner/repo` resolves the default branch via
  the API (learned that lesson the hard way).
- `irl doctor <pkg>` — checks network, disk, pip/npm presence before
  you install.
- `irl glasses <pkg>` — version/size/source lookup across registries.
- `irl rollback [ver]` — pick any published version from PyPI JSON,
  downgrade via a detached pip child.
- Safe extraction: named target dir, preview before writing, per-member
  zip-slip validation.

Silly (opt-in, but it's the brand):
- A grass streak with a GitHub-style heatmap, a terminal pet that gets
  moody if you skip days, daily quests, coins, 18 themes.
- Grassland Quest: a seeded garden-maze roguelike in pure Rich.
- Lofi Rhythm: a 4-lane beat game over 71 bundled lofi loops.

Technical bits: msvcrt/termios abstraction for input, winsound/
aplay/ffplay/afplay/paplay fallback chain for audio, no shell=True,
Python 3.8+, wheel is 976 KB. AGPL-3.0. Works on Linux/macOS/Windows
(CI: 3 OS × 5 Python versions).

Disclosure: I'm the author. Repo: https://github.com/Dev2Creator/IRL-

I'd genuinely like feedback on the installer routing UX — is auto-
sniffing a feature or a footgun? (There's `--help` everywhere and the
routes are deterministic.)

---

## 4. Reddit — r/Python

**Title**: I rebuilt my pip package into a 976KB terminal suite: universal installer, a Rich roguelike, a beat game from bundled WAVs, and a tamagotchi. AMA + would love a code review (AGPL)

**Body**:

A year ago I published irl-pkg, a jokey installer wrapper. It quietly
grew a following, and between versions 1.7.1–1.7.6 I made the classic
mistake of pushing to PyPI and not to GitHub — the source only existed
in the wheel. Recovering it (unpacking the PyPI wheel and diffing
against main) was humbling, and it kicked off a full v2.0 rebuild.

What's in the box, Python-wise:
- **irl/keys.py** — one keyboard abstraction: msvcrt on Windows,
  termios+tty on POSIX, normalized Key objects (UP/DOWN/ENTER/ESC/
  CTRL_C/CHAR...), non-TTY safe. The dashboard and games both sit on
  it.
- **irl/audio.py** — winsound → aplay → ffplay → afplay → paplay
  fallback chain, fire-and-forget Popen with arg lists, a looping
  thread for the rhythm game.
- **irl/grassland_quest.py** — ~400 lines, pure Rich: seeded recursive-
  backtracker maze, flood-fill-verified pickups, a turn-based boss
  ("The Deadline"). The seed makes charts/mazes deterministic, so
  tests are just... tests.
- **irl/rhythm.py** — beatmaps are derived from a SHA-256 of the
  filename + the WAV duration via the stdlib wave module. Same song,
  same chart, so high scores mean something.
- **irl/extract.py** — downloads and extracts into a named directory
  after a preview; every archive member is resolved and checked against
  the target dir (zip-slip), symlinks rejected, Content-Disposition
  filenames sanitized.
- **irl/rollback.py** — PyPI JSON API + questionary picker + detached
  `sys.executable -m pip` child (CREATE_NEW_PROCESS_GROUP via getattr,
  so it doesn't explode on POSIX).

Lessons I'd love feedback on:
1. Is normalizing keyboard input like this sane, or does someone have a
   better pattern?
2. My packaging: AGPL-3.0, `[tui]` extra for Textual, `requires-python
   >=3.8` — is 3.8 support worth it in 2026?
3. The coin/XP economy is all local JSON. Any prior art on
   gamified CLIs I should steal ideas from?

Repo (AGPL): https://github.com/Dev2Creator/IRL- — PyPI: irl-pkg.
Disclosure: I'm the author, Anika. Tests: 114 and green; CI on 3
OSes × Python 3.9–3.13.

---

## 5. Reddit — r/opensource

**Title**: IRL 2.0 — AGPL terminal tool, solo-maintained. Recovered my own lost source from a PyPI wheel, rebuilt, and open-sourced everything (CI, release automation, launch kit)

**Body**:

Solo-maintainer post. irl-pkg is a terminal command center (universal
package installer + an intentionally gamified layer: streaks, games, a
pet). It's AGPL-3.0, cross-platform, and the whole wheel is under 1 MB.

Three things might be interesting to this community:

1. **The lost-source recovery.** Versions 1.7.1–1.7.6 were published to
   PyPI but never pushed to GitHub. The fix: `pip download`, unpack the
   wheel, diff against main, commit the recovered tree as the baseline.
   The repo now matches PyPI again. Moral: your wheel is a backup, but
   an awful one.

2. **Release automation.** Tag v* → CI (ruff + pytest on 3 OS × Python
   3.9–3.13) → build → PyPI trusted publishing → GitHub Release
   generated from CHANGELOG.md. Zero tokens held by the maintainer
   beyond OIDC. Scripts in .github/workflows and scripts/release.sh —
   steal them.

3. **Sustainability of a joke project.** The gamification (grass
   streaks, pets, coins) is what keeps users, which keeps me
   maintaining the genuinely useful parts (the installer, doctor,
   rollback). Curious how others balance "serious core" with "the
   reason people actually show up".

Governance is simple: I'm the BDFL, AGPL for code, issues/PRs welcome,
CONTRIBUTING.md has the house rules (arg lists only, headers stay, no
heavy assets — the 12 MB DOS game zip that came with the 1.x wheel had
to ride into the sunset).

Repo: https://github.com/Dev2Creator/IRL- — I'm Anika, the maintainer.
