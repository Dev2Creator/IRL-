"""Shared fixtures: isolate every test from the developer's real home state."""

import os

import pytest


@pytest.fixture(autouse=True)
def isolated_home(tmp_path, monkeypatch):
    """Point all IRL state files at a temp dir for the duration of a test."""
    home = tmp_path / "home"
    home.mkdir()
    monkeypatch.setenv("HOME", str(home))
    monkeypatch.setenv("USERPROFILE", str(home))  # windows parity

    from irl import achievements, grass, pet, quests, rhythm, state

    monkeypatch.setattr(state, "STATE_FILE", str(home / ".irl_state.json"))
    monkeypatch.setattr(grass, "STATE_FILE", str(home / ".irl_grass.json"))
    monkeypatch.setattr(pet, "PET_FILE", str(home / ".irl_pet.json"))
    monkeypatch.setattr(quests, "QUESTS_FILE", str(home / ".irl_quests.json"))
    monkeypatch.setattr(achievements, "ACHIEVEMENTS_FILE", str(home / ".irl_achievements.json"))
    monkeypatch.setattr(rhythm, "SCORE_FILE", str(home / ".irl_rhythm.json"))

    # grassland_quest resolves its file via expanduser at call time.
    monkeypatch.setattr(os.path, "expanduser", lambda p: str(home / os.path.basename(p)))

    yield home


@pytest.fixture()
def seed_state(isolated_home):
    """A state file with a name so onboarding never hijacks the CLI."""
    from irl.state import save_state

    state = {
        "name": "Tester",
        "coins": 100,
        "active_banner": "default",
        "active_tone": "default",
        "active_color": "default",
        "purchased_banners": ["default"],
        "purchased_tones": ["default"],
        "purchased_colors": ["default"],
        "purchased_games": [],
        "total_xp": 0,
        "onboarded_v2": True,
    }
    save_state(state)
    return state
