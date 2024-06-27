# philiprehberger-clipboard

[![Tests](https://github.com/philiprehberger/py-clipboard/actions/workflows/publish.yml/badge.svg)](https://github.com/philiprehberger/py-clipboard/actions/workflows/publish.yml)
[![PyPI version](https://img.shields.io/pypi/v/philiprehberger-clipboard.svg)](https://pypi.org/project/philiprehberger-clipboard/)
[![Last updated](https://img.shields.io/github/last-commit/philiprehberger/py-clipboard)](https://github.com/philiprehberger/py-clipboard/commits/main)

Cross-platform clipboard copy and paste in one function call.

## Installation

```bash
pip install philiprehberger-clipboard
```

## Usage

```python
from philiprehberger_clipboard import copy, paste

copy("Hello, clipboard!")
text = paste()
print(text)  # Hello, clipboard!
```

### CLI

Copy text from stdin:

```bash
echo "Hello" | python -m philiprehberger_clipboard copy
```

Paste clipboard contents to stdout:

```bash
python -m philiprehberger_clipboard paste
```

Or use the installed script:

```bash
echo "Hello" | clipboard copy
clipboard paste
```

## API

| Function | Description |
|---|---|
| `copy(text: str) -> None` | Copy a string to the system clipboard |
| `paste() -> str` | Read a string from the system clipboard |
| `ClipboardError` | Raised when clipboard tool is unavailable or operation fails |

### Platform support

| Platform | Copy | Paste |
|---|---|---|
| Windows | `clip.exe` | PowerShell `Get-Clipboard` |
| macOS | `pbcopy` | `pbpaste` |
| Linux (X11) | `xclip` or `xsel` | `xclip` or `xsel` |
| Linux (Wayland) | `wl-copy` | `wl-paste` |

## Development

```bash
pip install -e .
python -m pytest tests/ -v
```

## Support

If you find this project useful:

⭐ [Star the repo](https://github.com/philiprehberger/py-clipboard)

🐛 [Report issues](https://github.com/philiprehberger/py-clipboard/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

💡 [Suggest features](https://github.com/philiprehberger/py-clipboard/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement)

❤️ [Sponsor development](https://github.com/sponsors/philiprehberger)

🌐 [All Open Source Projects](https://philiprehberger.com/open-source-packages)

💻 [GitHub Profile](https://github.com/philiprehberger)

🔗 [LinkedIn Profile](https://www.linkedin.com/in/philiprehberger)

## License

[MIT](LICENSE)
