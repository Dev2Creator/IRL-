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

"""Cross-platform audio playback for the IRL™ lofi empire.

Auto-detects the best backend available: winsound (Windows), aplay,
ffplay, afplay, paplay. All playback is fire-and-forget; nothing here
ever blocks the terminal or spawns a visible window. If no backend
exists the caller gets ``None``/False back and can say something nice
instead of crashing.
"""

import glob
import os
import random
import shutil
import subprocess

AUDIO_DIR = os.path.join(os.path.dirname(__file__), "assets", "audio")

_spawned = []  # playback processes we own, for stop_audio()


def _which(cmd):
    return shutil.which(cmd)


def _spawn(args, wait=False):
    kwargs = dict(
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
    )
    if os.name == "nt":
        kwargs["creationflags"] = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    process = subprocess.Popen(args, **kwargs)
    _spawned.append(process)
    if wait:
        process.wait()
    return True


def _play_winsound(path, wait):
    import winsound

    flags = winsound.SND_FILENAME
    flags |= winsound.SND_WAIT if wait else winsound.SND_ASYNC
    winsound.PlaySound(path, flags)
    return True


def _play_winmm_mp3(path, wait):
    import ctypes
    import time

    winmm = ctypes.windll.winmm
    alias = "irl_audio"
    winmm.mciSendStringW(f'open "{path}" type mpegvideo alias {alias}', None, 0, None)
    winmm.mciSendStringW(f"play {alias}", None, 0, None)
    if wait:
        time.sleep(0.5)  # MCI has no clean blocking play; caller polls
    return True


def play_wav(path, wait=False):
    """Play a WAV file. Returns True if a backend actually claimed it."""
    if not os.path.exists(path):
        return False
    if os.name == "nt":
        try:
            return _play_winsound(path, wait)
        except Exception:
            return False
    if _which("aplay"):
        return _spawn(["aplay", "-q", path], wait=wait)
    if _which("ffplay"):
        return _spawn(["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", path], wait=wait)
    if _which("afplay"):
        return _spawn(["afplay", path], wait=wait)
    if _which("paplay"):
        return _spawn(["paplay", path], wait=wait)
    return False


def play_mp3(path, wait=False):
    """Play an MP3 file. Returns True if a backend actually claimed it."""
    if not os.path.exists(path):
        return False
    if os.name == "nt":
        try:
            return _play_winmm_mp3(path, wait)
        except Exception:
            pass  # fall through to the unix-y attempts, weird but legal
    if _which("ffplay"):
        return _spawn(["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", path], wait=wait)
    if _which("afplay"):
        return _spawn(["afplay", path], wait=wait)
    if _which("paplay"):
        return _spawn(["paplay", path], wait=wait)
    return False


def play_wav_loop(path):
    """Loop a (short) WAV in a background thread until stop_audio().

    The bundled lofi files are 1-2s loops, so the rhythm game keeps them
    spinning for the length of a chart.
    """
    import threading

    global _stopped

    def _loop():
        while not _stopped:
            if not play_wav(path, wait=True):
                return

    _stopped = False
    thread = threading.Thread(target=_loop, daemon=True)
    _threads.append(thread)
    thread.start()
    return True


_threads = []
_stopped = False


def play_track(path, wait=False):
    """Play any supported audio file by extension."""
    ext = os.path.splitext(path)[1].lower()
    if ext == ".mp3":
        return play_mp3(path, wait=wait)
    return play_wav(path, wait=wait)


def list_lofi():
    """Sorted absolute paths of the bundled lofi WAVs."""
    return sorted(glob.glob(os.path.join(AUDIO_DIR, "*.wav")))


def play_random_lofi():
    """Play one random bundled lofi track. Returns the path, or None."""
    tracks = list_lofi()
    if not tracks:
        return None
    target = random.choice(tracks)
    return target if play_wav(target) else None


def stop_audio():
    """Best-effort stop of everything we started."""
    global _stopped
    _stopped = True
    for thread in _threads:
        try:
            thread.join(timeout=1.5)
        except Exception:
            pass
    _threads.clear()
    for process in _spawned:
        try:
            process.terminate()
        except Exception:
            pass
    _spawned.clear()
    if os.name == "nt":
        try:
            import winsound

            winsound.PlaySound(None, winsound.SND_PURGE)
        except Exception:
            pass
