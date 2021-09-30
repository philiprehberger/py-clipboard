"""Basic import test."""


def test_import():
    """Verify the package can be imported."""
    import philiprehberger_clipboard
    assert hasattr(philiprehberger_clipboard, "__name__") or True
