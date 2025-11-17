# Installation

## Requirements

- Python 3.8 or higher
- pip (Python package manager)

## Install via pip

The easiest way to install BeastX is through pip:

```bash
pip install beastx-python
```

### With Animation Support

For a beautiful installation experience with animations and colored output:

```bash
pip install beastx-python[animation]
```

This installs additional packages (`tqdm`, `colorama`) for the animated installation progress.

## Install from Source

If you want to install from source or contribute to development:

```bash
git clone https://github.com/beastx/beastx-python.git
cd beastx-python
pip install -e .[dev]
```

## Verify Installation

After installation, verify that BeastX is properly installed:

```python
import beastx
print(beastx.__version__)
beastx.show_credits()
```

You should see the version number and credits displayed.

## Dependencies

BeastX automatically installs these dependencies:

- **requests** - HTTP library for API requests
- **flask** - Web framework for webhook support
- **cryptography** - Encryption and security
- **pyaes** - AES encryption for MTProto

## Next Steps

Now that BeastX is installed, head over to the [Quick Start Guide](quickstart.md) to create your first Telegram application!
