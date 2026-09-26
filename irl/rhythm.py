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

"""Lofi Rhythm — a four-lane falling-note beat game.

Uses only the 71 bundled lofi WAVs (no new assets). The beatmap is
deterministically derived from the track's filename and duration, so a
given song always plays the same chart and high scores are fair.
Lanes: D F J K. Combos multiply. Scores persist in ~/.irl_rhythm.json.
"""

import hashlib
import json
import os
import random
import time
import wave

from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

from irl.audio import list_lofi, play_wav_loop, stop_audio
from irl.keys import is_interactive, read_char

console = Console()

SCORE_FILE = os.path.expanduser("~/.irl_rhythm.json")
LANES = ["d", "f", "j", "k"]
LANE_LABELS = "[bold cyan]D[/] [bold green]F[/] [bold yellow]J[/] [bold magenta]K[/]"
LANE_KEYS = {"d": 0, "f": 1, "j": 2, "k": 3}
NOTE = "[bold white]▼[/bold white] "
HIT_WINDOW = 0.42  # seconds a note waits at the judgment line


def load_scores():
    try:
        with open(SCORE_FILE, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_scores(scores):
    with open(SCORE_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f)


def track_duration(path):
    """WAV duration in seconds via the stdlib wave module."""
    try:
        with wave.open(path, "rb") as w:
            frames = w.getnframes()
            rate = w.getframerate() or 1
            return frames / rate
    except Exception:
        return 30.0  # a decent guess for a lofi loop


def make_chart(track_name, duration, density=1.4):
    """Deterministic note chart: list of (time, lane).

    Same song -> same chart. Hash seeds the RNG; notes are laid on a BPM
    grid with seeded skips so it grooves instead of machine-gunning.
    """
    seed = int(hashlib.sha256(track_name.encode()).hexdigest()[:12], 16)
    rng = random.Random(seed)
    bpm = rng.choice([72, 76, 80, 84, 88])
    beat = 60.0 / bpm
    notes = []
    t = beat * 4  # little intro
    end = min(duration - 1.0, 70.0)  # cap charts at a reasonable sprint
    while t < end:
        if rng.random() < density * 0.55:
            lane = rng.randrange(4)
            notes.append((round(t, 2), lane))
            if rng.random() < 0.18:  # occasional chord
                other = rng.choice([lane2 for lane2 in range(4) if lane2 != lane])
                notes.append((round(t, 2), other))
        t += beat
    return notes


def pick_track(preferred=None):
    tracks = list_lofi()
    if not tracks:
        return None
    if preferred:
        for t in tracks:
            if os.path.basename(t) == preferred:
                return t
    return random.choice(tracks)


def render(pending, score, combo, max_combo, judgments, now, title):
    """Build one frame: falling notes over 4 lanes + judgment line."""
    height = 14
    span = 4.0  # seconds a note is visible before the judgment line
    grid = [[" " for _ in range(4)] for _ in range(height)]
    for t, lane in pending:
        distance = t - now
        if distance < -HIT_WINDOW or distance > span:
            continue
        row = int(distance / span * (height - 1))
        grid[row][lane] = "▼"
    body = Text()
    for row in range(height):
        line = "".join(f"  {grid[row][lane]}  " for lane in range(4))
        style = "bold white on grey15" if row == height - 1 else "cyan"
        body.append(line + "\n", style=style)
    body.append("     ┴──┴──┴──┴", style="dim")
    stats = f"score {score:>6}   combo {combo:>3}x   best {max_combo:>3}x\nPERFECT {judgments.get('perfect', 0)}   GOOD {judgments.get('good', 0)}   MISS {judgments.get('miss', 0)}"
    return Panel(body, title=f"♪ {title}", subtitle=stats, border_style="cyan")


def play_chart(track_path, notes, duration):
    """Run one song. Returns (score, max_combo, judgments).

    ``duration`` is the chart length in seconds; audio loops underneath.
    """
    score = 0
    combo = 0
    max_combo = 0
    judgments = {"perfect": 0, "good": 0, "miss": 0}
    pending = sorted(notes)
    title = os.path.basename(track_path)

    start = time.monotonic()
    with Live(console=console, refresh_per_second=24) as live:
        while pending or time.monotonic() - start < duration:
            now = time.monotonic() - start
            # Expire notes past the window -> MISS
            while pending and pending[0][0] < now - HIT_WINDOW:
                pending.pop(0)
                combo = 0
                judgments["miss"] += 1
            # Drain input
            from irl.keys import kbhit, read_key

            while kbhit():
                try:
                    key = read_key()
                except EOFError:
                    return score, max_combo, judgments
                if key.is_char("q"):
                    return score, max_combo, judgments
                lane = LANE_KEYS.get(key.char.lower() if key.char else "")
                if lane is None:
                    continue
                hit = next(((t, ln) for (t, ln) in pending if ln == lane and abs(t - now) <= HIT_WINDOW), None)
                if hit:
                    pending.remove(hit)
                    delta = abs(hit[0] - now)
                    combo += 1
                    max_combo = max(max_combo, combo)
                    if delta < 0.12:
                        judgments["perfect"] += 1
                        score += 100 + combo * 5
                    else:
                        judgments["good"] += 1
                        score += 50 + combo * 2
                else:
                    combo = 0
            live.update(render(pending, score, combo, max_combo, judgments, now, title))
            time.sleep(0.04)
    return score, max_combo, judgments


def play_rhythm():
    if not is_interactive():
        console.print("[yellow]Lofi Rhythm needs a real terminal (and reflexes).[/yellow]")
        return
    track = pick_track()
    if track is None:
        console.print("[red]No lofi tracks found in the package. Someone deleted the vibe.[/red]")
        return
    # The bundled WAVs are short loops: the chart runs a fixed-length song
    # and the audio keeps looping underneath until stop_audio().
    song_length = 60.0
    chart = make_chart(os.path.basename(track), song_length)
    title = os.path.basename(track)
    best = load_scores().get(title, 0)

    console.print(
        Panel(
            f"[bold cyan]♪ LOFI RHYTHM ♪[/bold cyan]\n\n"
            f"Track: [bold]{title}[/bold]\n"
            f"Lanes: {LANE_LABELS}   (Q to quit mid-song)\n"
            f"Personal best on this track: [bold yellow]{best}[/bold yellow]\n\n"
            f"[dim]Notes fall; tap the lane key when ▼ crosses the bottom line.\n"
            f"The chart is deterministic: same song, same map. Practice makes perfect.[/dim]",
            border_style="cyan",
        )
    )
    console.print("[dim]Press any lane key to start...[/dim]")
    read_char(default="\n")

    play_wav_loop(track)
    try:
        score, max_combo, judgments = play_chart(track, chart, song_length)
    finally:
        stop_audio()

    scores = load_scores()
    previous = scores.get(title, 0)
    scores[title] = max(previous, score)
    save_scores(scores)

    rank = "🥇 Certified Groover" if score >= 4000 else "🥈 Beat Enjoyer" if score >= 2000 else "🥉 Lofi Apprentice"
    console.print(
        Panel(
            f"[bold]Score: {score}[/bold]  (best: {scores[title]})\nMax combo: {max_combo}x — PERFECT {judgments['perfect']} / GOOD {judgments['good']} / MISS {judgments['miss']}\n{rank}",
            title="results",
            border_style="green" if score > previous else "yellow",
        )
    )
    from irl.state import add_coins

    add_coins(score // 20, "Lofi Rhythm performance")
    try:
        from irl.achievements import check_auto

        check_auto(context={"game": "rhythm_score", "score": score})
    except Exception:
        pass
