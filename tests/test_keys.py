"""keys.py normalization: pure POSIX mapping + non-tty behavior."""

import pytest

from irl import keys as K


def test_named_key_mapping(monkeypatch):
    monkeypatch.setattr(K, "_select_byte", lambda timeout: None)  # no escape sequences here
    assert K._normalize_posix("\r") == K.KEY_ENTER
    assert K._normalize_posix("\n") == K.KEY_ENTER
    assert K._normalize_posix(" ") == K.KEY_SPACE
    assert K._normalize_posix("\t") == K.KEY_TAB
    assert K._normalize_posix("\x7f") == K.KEY_BACKSPACE
    assert K._normalize_posix("\x08") == K.KEY_BACKSPACE
    assert K._normalize_posix("\x03") == K.KEY_CTRL_C
    assert K._normalize_posix("\x04") == K.KEY_CTRL_D
    assert K._normalize_posix("") == K.KEY_EOF
    assert K._normalize_posix("\x1b") == K.KEY_ESC


def test_char_keys_case_preserved():
    key = K._normalize_posix("q")
    assert key.is_char("q")
    assert not key.is_char("w")
    upper = K._normalize_posix("Q")
    assert upper.is_char("Q")


def test_arrow_escape_parsing(monkeypatch):
    monkeypatch.setattr(
        K,
        "_select_byte",
        lambda timeout: "[",
    )
    monkeypatch.setattr(K, "_select_byte", lambda timeout: "[")  # first peek
    # Simulate: ESC then [ then A
    seq = iter(["[", "A"])
    monkeypatch.setattr(K, "_select_byte", lambda timeout: next(seq))
    assert K._normalize_posix("\x1b") == K.KEY_UP


def test_arrow_down_parsing(monkeypatch):
    seq = iter(["[", "B"])
    monkeypatch.setattr(K, "_select_byte", lambda timeout: next(seq))
    assert K._normalize_posix("\x1b") == K.KEY_DOWN


def test_lone_escape_returns_esc(monkeypatch):
    monkeypatch.setattr(K, "_select_byte", lambda timeout: None)
    assert K._normalize_posix("\x1b") == K.KEY_ESC


def test_unknown_bytes_map_to_unknown():
    assert K._normalize_posix("\x00").name == K.UNKNOWN
    assert K._normalize_posix("\x01").name == K.UNKNOWN


def test_non_interactive_read_key_raises():
    with pytest.raises(EOFError):
        K.read_key()


def test_read_char_eof_default():
    assert K.read_char(default="q") == "q"


def test_key_equality_and_hash():
    assert K.Key(K.CHAR, "a") == K.Key(K.CHAR, "a")
    assert K.Key(K.CHAR, "a") != K.Key(K.CHAR, "b")
    assert len({K.KEY_UP, K.KEY_UP, K.KEY_DOWN}) == 2
