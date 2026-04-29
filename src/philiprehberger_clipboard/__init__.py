"""Cross-platform clipboard copy and paste in one function call."""

from __future__ import annotations

import shutil
import subprocess
import sys

__all__ = ["copy", "paste", "is_available", "ClipboardError"]


class ClipboardError(RuntimeError):
    """Raised when a clipboard tool is not available or an operation fails."""


def _get_linux_copy_cmd() -> list[str]:
    """Return the command list for copying on Linux."""
    if shutil.which("xclip"):
        return ["xclip", "-selection", "clipboard"]
    if shutil.which("xsel"):
        return ["xsel", "--clipboard", "--input"]
    if shutil.which("wl-copy"):
        return ["wl-copy"]
    raise ClipboardError(
        "No clipboard tool found. Install xclip, xsel, or wl-clipboard."
    )


def _get_linux_paste_cmd() -> list[str]:
    """Return the command list for pasting on Linux."""
    if shutil.which("xclip"):
        return ["xclip", "-selection", "clipboard", "-o"]
    if shutil.which("xsel"):
        return ["xsel", "--clipboard", "--output"]
    if shutil.which("wl-paste"):
        return ["wl-paste"]
    raise ClipboardError(
        "No clipboard tool found. Install xclip, xsel, or wl-clipboard."
    )


def is_available() -> bool:
    """Return True if a clipboard backend is detected on the current platform.

    Lets callers feature-test before invoking :func:`copy` or :func:`paste`
    instead of catching :class:`ClipboardError`.

    Returns:
        ``True`` if a known clipboard tool is available, ``False`` otherwise.
    """
    if sys.platform == "win32":
        return shutil.which("clip.exe") is not None and shutil.which("powershell.exe") is not None
    if sys.platform == "darwin":
        return shutil.which("pbcopy") is not None and shutil.which("pbpaste") is not None
    return any(
        shutil.which(tool) is not None
        for tool in ("xclip", "xsel", "wl-copy", "wl-paste")
    )


def copy(text: str) -> None:
    """Copy a string to the system clipboard.

    Args:
        text: The string to place on the clipboard.

    Raises:
        ClipboardError: If the clipboard tool is unavailable or the operation fails.
    """
    try:
        if sys.platform == "win32":
            subprocess.run(
                ["clip.exe"],
                input=text,
                check=True,
                capture_output=True,
                text=True,
            )
        elif sys.platform == "darwin":
            subprocess.run(
                ["pbcopy"],
                input=text,
                check=True,
                capture_output=True,
                text=True,
            )
        else:
            cmd = _get_linux_copy_cmd()
            subprocess.run(
                cmd,
                input=text,
                check=True,
                capture_output=True,
                text=True,
            )
    except FileNotFoundError as exc:
        raise ClipboardError(f"Clipboard tool not found: {exc}") from exc
    except subprocess.CalledProcessError as exc:
        raise ClipboardError(f"Clipboard copy failed: {exc}") from exc


def paste() -> str:
    """Read a string from the system clipboard.

    Returns:
        The current clipboard contents as a string.

    Raises:
        ClipboardError: If the clipboard tool is unavailable or the operation fails.
    """
    try:
        if sys.platform == "win32":
            result = subprocess.run(
                ["powershell.exe", "-Command", "Get-Clipboard"],
                check=True,
                capture_output=True,
                text=True,
            )
        elif sys.platform == "darwin":
            result = subprocess.run(
                ["pbpaste"],
                check=True,
                capture_output=True,
                text=True,
            )
        else:
            cmd = _get_linux_paste_cmd()
            result = subprocess.run(
                cmd,
                check=True,
                capture_output=True,
                text=True,
            )
    except FileNotFoundError as exc:
        raise ClipboardError(f"Clipboard tool not found: {exc}") from exc
    except subprocess.CalledProcessError as exc:
        raise ClipboardError(f"Clipboard paste failed: {exc}") from exc

    return result.stdout
