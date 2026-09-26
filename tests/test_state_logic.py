"""Grass streaks, coins, pets, quests, achievements — the state machine zoo."""

from datetime import datetime, timedelta

from irl import grass
from irl.achievements import ACHIEVEMENTS, award, get_level, load_unlocked
from irl.quests import generate_quests, load_board, report
from irl.state import add_coins, load_state


def _grass(**overrides):
    return {"last_touched": None, "streak": 0, "xp": 0, **overrides}


def test_grass_first_touch_sets_streak_one(isolated_home, seed_state):
    grass.save_state(_grass())
    grass.touch_grass()
    state = grass.load_state()
    assert state["streak"] == 1
    assert state["last_touched"] == datetime.now().strftime("%Y-%m-%d")


def test_grass_once_daily_gate(isolated_home, seed_state):
    today = datetime.now().strftime("%Y-%m-%d")
    grass.save_state(_grass(last_touched=today, streak=3, xp=3))
    grass.touch_grass()
    assert grass.load_state()["streak"] == 3  # unchanged


def test_grass_consecutive_day_extends(isolated_home, seed_state):
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    grass.save_state(_grass(last_touched=yesterday, streak=5, xp=5))
    grass.touch_grass()
    assert grass.load_state()["streak"] == 6


def test_grass_gap_resets_streak(isolated_home, seed_state):
    long_ago = (datetime.now() - timedelta(days=4)).strftime("%Y-%m-%d")
    grass.save_state(_grass(last_touched=long_ago, streak=9, xp=9))
    grass.touch_grass()
    assert grass.load_state()["streak"] == 1


def test_grass_history_recorded_for_heatmap(isolated_home, seed_state):
    grass.save_state(_grass())
    grass.touch_grass()
    today = datetime.now().strftime("%Y-%m-%d")
    assert grass.load_state()["history"][today] == 1


def test_grass_ranks():
    assert grass.get_rank(0) == "🌿 Rookie Grass Toucher"
    assert grass.get_rank(7) == "🪴 Weekend Gardener"
    assert grass.get_rank(365) == "👑 Legendary Lawn Master"


def test_add_coins_can_be_negative(isolated_home, seed_state):
    add_coins(-40)
    assert load_state()["coins"] == 60


def test_pet_stages(isolated_home, seed_state):
    from irl.pet import _stage

    egg = {"care": 0, "streak_seen": 0}
    ascended = {"care": 35, "streak_seen": 30}
    assert _stage(egg) == "egg"
    assert _stage(ascended) == "ascended"


def test_pet_sulks_when_skipped(isolated_home, seed_state):
    from datetime import datetime

    from irl.pet import _mood

    old = {"hunger": 0, "last_seen": "2001-01-01"}
    assert _mood(old) == "sulk"
    fresh = {"hunger": 0, "last_seen": datetime.now().strftime("%Y-%m-%d")}
    assert _mood(fresh) in ("happy", "hungry")


def test_quests_deterministic_per_day():
    a = generate_quests("2026-09-27")
    b = generate_quests("2026-09-27")
    assert [q["id"] for q in a] == [q["id"] for q in b]
    assert len(a) == 3
    assert {q["id"] for q in generate_quests("2026-01-01")} != set()  # any day yields a board


def test_quest_report_pays_and_completes(isolated_home, seed_state):
    before = load_state()["coins"]
    board = load_board()
    quest_id = board["today"][0]["id"]
    assert report(quest_id) is True
    after = load_state()["coins"]
    assert after > before
    board = load_board()
    assert next(q for q in board["today"] if q["id"] == quest_id)["done"]


def test_quest_report_idempotent(isolated_home, seed_state):
    quest_id = load_board()["today"][0]["id"]
    coins_mid = None
    report(quest_id)
    coins_mid = load_state()["coins"]
    report(quest_id)
    assert load_state()["coins"] == coins_mid


def test_achievement_award_pays_once(isolated_home, seed_state):
    before = load_state()["coins"]
    assert award("first_install") is True
    mid = load_state()["coins"]
    assert award("first_install") is False
    assert load_state()["coins"] == mid
    assert mid > before
    assert "first_install" in load_unlocked()


def test_level_ladder():
    assert get_level({"total_xp": 0})[1] == "Noob"
    assert get_level({"total_xp": 301})[1] == "Code Gremlin"
    assert get_level({"total_xp": 1501})[1] == "10x Dev"
    assert get_level({"total_xp": 99999})[1] == "Grass Sensei"


def test_achievement_catalog_complete():
    assert len(ACHIEVEMENTS) == 12
    for ach_id, (title, desc, reward) in ACHIEVEMENTS.items():
        assert title and desc and reward > 0
