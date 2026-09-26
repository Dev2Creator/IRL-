"""Zip-slip and archive extraction security."""

import tarfile
import zipfile

import pytest

from irl.extract import (
    UnsafeArchiveError,
    _member_target,
    _sanitize_filename,
    safe_extract,
)


@pytest.fixture()
def target(tmp_path):
    d = tmp_path / "target"
    d.mkdir()
    return d


def _make_zip(path, members):
    with zipfile.ZipFile(path, "w") as z:
        for name, content in members.items():
            z.writestr(name, content)


def test_clean_zip_extracts_into_named_dir(tmp_path, target):
    archive = tmp_path / "pkg.zip"
    _make_zip(archive, {"pkg/main.py": "print(1)", "pkg/readme.md": "hi"})
    assert safe_extract(archive, target, assume_yes=True)
    assert (target / "pkg" / "main.py").read_text() == "print(1)"


def test_zip_slip_rejected(tmp_path, target):
    archive = tmp_path / "evil.zip"
    _make_zip(archive, {"../../pwned.txt": "x", "ok.txt": "fine"})
    with pytest.raises(UnsafeArchiveError):
        safe_extract(archive, target, assume_yes=True)
    assert not (tmp_path / "pwned.txt").exists()


def test_zip_absolute_path_rejected(tmp_path, target):
    archive = tmp_path / "evil2.zip"
    _make_zip(archive, {"/etc/irl_pwned": "x"})
    with pytest.raises(UnsafeArchiveError):
        safe_extract(archive, target, assume_yes=True)


@pytest.mark.parametrize("bad", ["/etc/passwd", "../evil", "a/../../b", "..\\..\\win_evil", "C:\\evil.txt"])
def test_member_validation_rejects_all_tricks(tmp_path, bad):
    with pytest.raises(UnsafeArchiveError):
        _member_target(str(tmp_path), bad)


def test_tar_with_symlink_rejected(tmp_path, target):
    archive = tmp_path / "link.tar"
    payload = tmp_path / "payload.txt"
    payload.write_text("x")
    with tarfile.open(archive, "w") as tf:
        tf.add(payload, arcname="payload.txt")
        info = tarfile.TarInfo("link")
        info.type = tarfile.SYMTYPE
        info.linkname = "/etc/passwd"
        tf.addfile(info)
    with pytest.raises(UnsafeArchiveError):
        safe_extract(archive, target, assume_yes=True)


def test_clean_tar_extracts(tmp_path, target):
    archive = tmp_path / "plain.tar"
    payload = tmp_path / "plain.txt"
    payload.write_text("content")
    with tarfile.open(archive, "w") as tf:
        tf.add(payload, arcname="plain.txt")
    assert safe_extract(archive, target, assume_yes=True)
    assert (target / "plain.txt").read_text() == "content"


def test_invalid_archive_returns_false(tmp_path, target):
    junk = tmp_path / "junk.zip"
    junk.write_text("not an archive")
    assert safe_extract(junk, target, assume_yes=True) is False


def test_filename_sanitizer():
    assert _sanitize_filename('attachment; filename="../../evil.sh"', "https://x/y") == "evil.sh"
    assert _sanitize_filename(None, "https://example.com/pkg-main.zip") == "pkg-main.zip"
    assert "/" not in _sanitize_filename("attachment; filename=a/b/c.zip", "u")
    assert _sanitize_filename(None, "https://x/y") == "y"  # falls back to URL basename
    assert _sanitize_filename(None, "https://example.com/a/really-long-name.zip") == "really-long-name.zip"
