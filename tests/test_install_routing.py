"""Installer routing: URL / owner-repo / PyPI / npm / search fallback."""

import pytest

import irl.install as install_mod
from irl.state import load_state


@pytest.fixture()
def recorder(monkeypatch):
    calls = []

    def fake_download(url, *a, **kw):
        calls.append(url)

    monkeypatch.setattr(install_mod, "download_and_extract", fake_download)
    return calls


def _registry(monkeypatch, pypi=False, npm=False):
    def fake_check(url):
        if "pypi.org" in url:
            return pypi
        if "registry.npmjs.org" in url:
            return npm
        return False

    monkeypatch.setattr(install_mod, "check_registry", fake_check)


def test_direct_url_routes_to_download(recorder):
    install_mod.install_package("https://example.com/pkg.zip")
    assert recorder == ["https://example.com/pkg.zip"]


def test_owner_slash_repo_builds_github_zip(recorder):
    install_mod.install_package("octocat/Hello-World")
    assert recorder == ["https://github.com/octocat/Hello-World/archive/refs/heads/main.zip"]


def test_scoped_npm_name_not_treated_as_repo(recorder, monkeypatch):
    """`@scope/pkg` starts with @ so it must NOT hit the GitHub branch."""
    _registry(monkeypatch, pypi=False, npm=False)
    monkeypatch.setattr(install_mod.requests, "get", lambda *a, **kw: type("R", (), {"status_code": 404})())
    install_mod.install_package("@scope/pkg")
    assert recorder == []  # falls through npm probe and search, no repo URL


def test_pypi_route_installs_via_pip(recorder, monkeypatch, seed_state):
    _registry(monkeypatch, pypi=True)
    monkeypatch.setattr(install_mod, "install_pip", lambda pkg: True)
    install_mod.install_package("requests")
    assert recorder == []
    assert load_state()["coins"] >= 110  # starting 100 + install reward


def test_npm_route(recorder, monkeypatch, seed_state):
    _registry(monkeypatch, pypi=False, npm=True)
    monkeypatch.setattr(install_mod, "install_npm", lambda pkg: True)
    install_mod.install_package("express")
    assert load_state()["coins"] >= 110


def test_pypi_failure_does_not_reward(recorder, monkeypatch, seed_state):
    _registry(monkeypatch, pypi=True)
    monkeypatch.setattr(install_mod, "install_pip", lambda pkg: False)
    install_mod.install_package("requests")
    assert load_state()["coins"] == 100


def test_fallback_github_search(recorder, monkeypatch, seed_state):
    _registry(monkeypatch, pypi=False, npm=False)

    class FakeResponse:
        status_code = 200

        def json(self):
            return {"items": [{"full_name": "some/Repo", "default_branch": "master"}]}

    monkeypatch.setattr(install_mod.requests, "get", lambda *a, **kw: FakeResponse())
    install_mod.install_package("weird-package-name")
    assert recorder == ["https://github.com/some/Repo/archive/refs/heads/master.zip"]


def test_unknown_package_neither_installs_nor_crashes(recorder, monkeypatch, seed_state):
    _registry(monkeypatch, pypi=False, npm=False)

    class FakeResponse:
        status_code = 200

        def json(self):
            return {"items": []}

    monkeypatch.setattr(install_mod.requests, "get", lambda *a, **kw: FakeResponse())
    install_mod.install_package("totally-not-a-package-xyz")
    assert recorder == []
