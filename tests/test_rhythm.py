"""Lofi Rhythm: charting determinism and score persistence."""

import json

from irl.rhythm import HIT_WINDOW, load_scores, make_chart, save_scores, track_duration


def test_chart_deterministic_same_song():
    a = make_chart("70.wav", 60.0)
    b = make_chart("70.wav", 60.0)
    assert a == b


def test_chart_differs_between_songs():
    assert make_chart("70.wav", 60.0) != make_chart("12.wav", 60.0)


def test_chart_notes_within_lanes_and_time():
    notes = make_chart("70.wav", 60.0)
    assert len(notes) > 30
    for t, lane in notes:
        assert 0 <= lane <= 3
        assert t > 0


def test_hit_window_sane():
    assert 0.05 <= HIT_WINDOW <= 0.6


def test_track_duration_real_wav():
    import os

    from irl.audio import list_lofi

    tracks = list_lofi()
    if tracks:
        d = track_duration(tracks[0])
        assert 0.1 < d < 60  # the loops are short


def test_track_duration_fallback():
    assert track_duration("/nonexistent/whatever.wav") == 30.0


def test_score_persistence(tmp_path):
    save_scores({"70.wav": 1234})
    assert load_scores()["70.wav"] == 1234
    data = json.load(open(str(tmp_path / ".irl_rhythm.json"), encoding="utf-8")) if (tmp_path / ".irl_rhythm.json").exists() else load_scores()
    assert data["70.wav"] == 1234
