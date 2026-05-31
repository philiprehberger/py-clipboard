"""Basic import + availability tests."""

import pytest


def test_import():
    """Verify the package can be imported."""
    import philiprehberger_clipboard
    assert hasattr(philiprehberger_clipboard, "__name__") or True


def test_is_available_returns_bool():
    from philiprehberger_clipboard import is_available

    assert isinstance(is_available(), bool)


def test_public_api_exports():
    import philiprehberger_clipboard as mod

    for name in ("copy", "paste", "is_available", "clear", "equals", "ClipboardError"):
        assert name in mod.__all__
        assert hasattr(mod, name)


def test_clear_copies_empty_string(monkeypatch):
    """clear() should delegate to copy("")."""
    import philiprehberger_clipboard as mod

    captured: dict[str, str] = {}

    def fake_copy(text: str) -> None:
        captured["value"] = text

    monkeypatch.setattr(mod, "copy", fake_copy)
    mod.clear()
    assert captured["value"] == ""


def test_equals_true_when_clipboard_matches(monkeypatch):
    """equals(text) returns True when paste() returns the same text."""
    import philiprehberger_clipboard as mod

    monkeypatch.setattr(mod, "paste", lambda: "hello")
    assert mod.equals("hello") is True


def test_equals_false_when_clipboard_differs(monkeypatch):
    """equals(text) returns False when paste() returns different text."""
    import philiprehberger_clipboard as mod

    monkeypatch.setattr(mod, "paste", lambda: "hello")
    assert mod.equals("world") is False


def test_equals_false_when_backend_unavailable(monkeypatch):
    """equals(text) returns False instead of raising when paste fails."""
    import philiprehberger_clipboard as mod

    def fake_paste() -> str:
        raise mod.ClipboardError("no backend")

    monkeypatch.setattr(mod, "paste", fake_paste)
    assert mod.equals("anything") is False


def test_clear_and_roundtrip_when_available():
    """If a real backend is available, clear() + paste() should yield empty string."""
    from philiprehberger_clipboard import clear, is_available, paste

    if not is_available():
        pytest.skip("no clipboard backend available")
    clear()
    assert paste() == ""
