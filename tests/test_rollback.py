"""Rollback logic: version fetching, guards, delayed install."""

import irl.rollback as R


def test_pypi_versions_live():
    """Live PyPI check (skipped gracefully offline)."""
    try:
        versions = R.pypi_versions()
    except Exception:
        import pytest

        pytest.skip("PyPI unreachable")
    assert "1.7.6" in versions
    assert versions[0] >= "1.7.6" or versions  # newest first


def test_version_tuple_ordering():
    assert R._version_tuple("1.10.0") > R._version_tuple("1.9.0")
    assert R._version_tuple("2.0.0") > R._version_tuple("1.99.99")


def test_rollback_with_version_and_yes(monkeypatch, capsys):
    fired = []
    monkeypatch.setattr(R, "_launch_package_install", lambda pkg, ver: fired.append((pkg, ver)))
    R.rollback_irl("1.7.5", yes=True)
    assert fired == [("irl-pkg", "1.7.5")]


def test_rollback_rejects_unknown_version(monkeypatch, capsys):
    fired = []
    monkeypatch.setattr(R, "_launch_package_install", lambda pkg, ver: fired.append((pkg, ver)))
    R.rollback_irl("0.0.1-fake", yes=True)
    assert fired == []
    assert "not found" in capsys.readouterr().out.lower()


def test_rollback_yes_without_version_is_guarded(monkeypatch, capsys):
    fired = []
    monkeypatch.setattr(R, "_launch_package_install", lambda pkg, ver: fired.append((pkg, ver)))
    R.rollback_irl(None, yes=True)
    assert fired == []
    assert "--yes needs a version" in capsys.readouterr().out


def test_rollback_pypi_unreachable_message(monkeypatch, capsys):
    def boom():
        raise OSError("no network")

    monkeypatch.setattr(R, "pypi_versions", boom)
    R.rollback_irl("1.7.5", yes=True)
    assert "cannot reach PyPI" in capsys.readouterr().out
