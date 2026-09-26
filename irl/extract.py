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

"""Downloading and archive extraction — the paranoid edition.

Extraction targets a NAMED directory (never the CWD), every member is
validated against path traversal ("zip-slip") and symlink tricks, and
you get a preview of what will be written before anything touches disk.
"""

import os
import tarfile
import urllib.parse
import zipfile

import requests
from rich.panel import Panel
from rich.progress import DownloadColumn, Progress, TextColumn, TransferSpeedColumn


class UnsafeArchiveError(Exception):
    """Raised when an archive tries to escape its target directory."""


def _sanitize_filename(content_disposition, url):
    """A filename we actually asked for, not one the server made up."""
    filename = "downloaded_package"
    if content_disposition and "filename=" in content_disposition:
        filename = content_disposition.split("filename=")[1].strip("\"' ")
    else:
        parsed = urllib.parse.urlparse(url)
        base = os.path.basename(parsed.path)
        if base:
            filename = base
    # Servers have submitted nonsense before; keep only the tail.
    filename = os.path.basename(filename.replace("\\", "/")).strip(". ")
    filename = "".join(c if c.isalnum() or c in "._-" else "_" for c in filename)[:100]
    return filename or "downloaded_package"


def _member_target(target_dir, member_name):
    """Resolve where a member would land; raise if it escapes target_dir.

    Works for zip and tar member names alike ('../evil', '/etc/passwd',
    'C:\\evil', 'a/../../b').
    """
    name = member_name.replace("\\", "/")
    if name.startswith("/") or (len(name) > 1 and name[1] == ":"):
        raise UnsafeArchiveError(f"absolute path in archive: {member_name!r}")
    dest = os.path.realpath(os.path.join(target_dir, name))
    target_real = os.path.realpath(target_dir) + os.sep
    if not (dest == os.path.realpath(target_dir) or dest.startswith(target_real)):
        raise UnsafeArchiveError(f"path traversal in archive: {member_name!r}")
    return dest


def _validate_zip(zip_path, target_dir):
    with zipfile.ZipFile(zip_path) as zf:
        for info in zf.infolist():
            _member_target(target_dir, info.filename)


def _validate_tar(tar_path, target_dir):
    with tarfile.open(tar_path, "r:*") as tf:
        for member in tf.getmembers():
            _member_target(target_dir, member.name)
            if member.issym() or member.islnk():
                raise UnsafeArchiveError(f"link member in archive: {member.name!r}")


def archive_preview(archive_path):
    """One-line-per-entry style preview: top entries + totals."""
    entries = []
    total = 0
    if zipfile.is_zipfile(archive_path):
        with zipfile.ZipFile(archive_path) as zf:
            infos = zf.infolist()
            total = sum(i.file_size for i in infos)
            entries = [i.filename for i in infos[:8]]
            count = len(infos)
    elif tarfile.is_tarfile(archive_path):
        with tarfile.open(archive_path, "r:*") as tf:
            members = tf.getmembers()
            total = sum(m.size for m in members)
            entries = [m.name for m in members[:8]]
            count = len(members)
    else:
        return None
    more = f"\n  … and {count - 8} more" if count > 8 else ""
    listing = "".join(f"\n  {e}" for e in entries) + more
    return f"Archive: [bold]{os.path.basename(archive_path)}[/bold]\nEntries: {count}   Uncompressed: {total / 1024 / 1024:.1f} MB\nContents:{listing}"


def safe_extract(archive_path, target_dir, assume_yes=False):
    """Preview, confirm, then extract into ``target_dir`` (zip-slip safe)."""
    if not (zipfile.is_zipfile(archive_path) or tarfile.is_tarfile(archive_path)):
        return False

    os.makedirs(target_dir, exist_ok=True)
    preview = archive_preview(archive_path)
    if preview:
        print(Panel(preview, title="What lands on your disk", border_style="#F29265"))

    if not assume_yes:
        from rich.prompt import Prompt

        approved = Prompt.ask("Extract here? [y/N]", default="no").strip().lower() in ("y", "yes")
        if not approved:
            print("Extraction cancelled. The archive stays put, unloved.")
            return False

    if zipfile.is_zipfile(archive_path):
        _validate_zip(archive_path, target_dir)
        with zipfile.ZipFile(archive_path) as zf:
            zf.extractall(target_dir)  # noqa: S202 - every member validated in _validate_zip above
    else:
        _validate_tar(archive_path, target_dir)
        with tarfile.open(archive_path, "r:*") as tf:
            tf.extractall(target_dir)  # noqa: S202 - every member validated in _validate_tar above
    return True


def download_and_extract(url):
    from irl.state import load_state  # noqa: F401  (kept for parity with 1.x behavior)

    print(f"\nDownloading from {url}...")
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        response = requests.get(url, headers=headers, stream=True, timeout=30)
        response.raise_for_status()

        total_size = int(response.headers.get("content-length", 0))
        filename = _sanitize_filename(response.headers.get("content-disposition"), url)

        with Progress(TextColumn("[bold blue]🌱 Touching grass..."), "[progress.percentage]{task.percentage:>3.0f}%", DownloadColumn(), TransferSpeedColumn()) as progress:
            _task = progress.add_task("Downloading", total=total_size)
            with open(filename, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
                        progress.update(_task, advance=len(chunk))

        # Named target dir (no more spraying files into the CWD).
        stem = os.path.splitext(filename)[0].rstrip(".-") or "package"
        target_dir = os.path.abspath(stem)

        extracted = safe_extract(filename, target_dir)
        if extracted:
            os.remove(filename)
            print(f"✨ Successfully touched grass! Package lives at: {target_dir}")
        else:
            print("❌ Downloaded file was not a valid archive. Could not extract.")

    except UnsafeArchiveError as e:
        print(f"❌ Blocked a suspicious archive ({e}). It has been reported to the grass.")
        _cleanup_partial(filename)
    except Exception as e:
        print(f"❌ Error during download/extraction: {e}")
        _cleanup_partial(filename)


def _cleanup_partial(filename):
    """Best-effort removal of a download we no longer trust."""
    try:
        if os.path.exists(filename):
            os.remove(filename)
    except OSError:
        pass
