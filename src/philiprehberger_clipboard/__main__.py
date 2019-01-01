"""CLI interface: python -m philiprehberger_clipboard copy/paste"""

from __future__ import annotations

import sys

from . import copy, paste


def main() -> None:
    if len(sys.argv) < 2 or sys.argv[1] not in ("copy", "paste"):
        print("Usage: python -m philiprehberger_clipboard [copy|paste]", file=sys.stderr)
        sys.exit(1)
    if sys.argv[1] == "copy":
        text = sys.stdin.read()
        copy(text)
    else:
        print(paste())


if __name__ == "__main__":
    main()
