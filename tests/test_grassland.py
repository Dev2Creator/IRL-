"""Grassland Quest: maze generation and streak extension."""

from collections import deque
from datetime import datetime

from irl.grassland_quest import (
    SUN_NEEDED,
    WATER_NEEDED,
    extend_grass_streak,
    generate_maze,
    place_items,
)


def _reachable(grid):
    seen = {(1, 1)}
    q = deque([(1, 1)])
    h, w = len(grid), len(grid[0])
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and grid[ny][nx] in ".E" and (nx, ny) not in seen:
                seen.add((nx, ny))
                q.append((nx, ny))
    return seen


def test_maze_deterministic_per_seed():
    assert generate_maze(seed=7) == generate_maze(seed=7)


def test_maze_different_seeds_differ():
    assert generate_maze(seed=1) != generate_maze(seed=2)


def test_maze_has_bordered_walls_and_start():
    grid = generate_maze(seed=3)
    assert grid[0][0] == "#"
    assert grid[1][1] == "."
    assert all(grid[0][x] == "#" for x in range(len(grid[0])))
    assert all(grid[y][0] == "#" for y in range(len(grid)))


def test_all_pickups_and_boss_reachable():
    for seed in range(5):
        grid = generate_maze(seed=seed)
        water, sun, bugs, boss = place_items(grid, seed=seed)
        seen = _reachable(grid)
        assert len(water) == WATER_NEEDED
        assert len(sun) == SUN_NEEDED
        assert all(p in seen for p in water + sun)
        assert boss in seen


def test_pickups_never_spawn_on_start():
    grid = generate_maze(seed=99)
    water, sun, _bugs, boss = place_items(grid, seed=99)
    assert (1, 1) not in water + sun
    assert boss != (1, 1)


def test_boss_chamber_has_exit():
    grid = generate_maze(seed=11)
    exit_cells = [(x, y) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == "E"]
    assert len(exit_cells) == 1


def test_extend_grass_streak_adds_and_records(isolated_home, seed_state):
    streak = extend_grass_streak(1)
    today = datetime.now().strftime("%Y-%m-%d")
    assert streak == 1  # fresh home, no prior grass file
    streak2 = extend_grass_streak(1)
    assert streak2 == 2
    import json
    import os

    data = json.load(open(os.path.expanduser("~/.irl_grass.json"), encoding="utf-8"))
    assert data["history"][today] == 2
