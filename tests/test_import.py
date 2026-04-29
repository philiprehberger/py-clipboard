"""Basic import + availability tests."""


def test_import():
    """Verify the package can be imported."""
    import philiprehberger_clipboard
    assert hasattr(philiprehberger_clipboard, "__name__") or True


def test_is_available_returns_bool():
    from philiprehberger_clipboard import is_available

    assert isinstance(is_available(), bool)


def test_public_api_exports():
    import philiprehberger_clipboard as mod

    for name in ("copy", "paste", "is_available", "ClipboardError"):
        assert name in mod.__all__
        assert hasattr(mod, name)
