# ⚡ BeastX - Powerful Telegram Client Library

<div align="center">

![BeastX Logo](https://via.placeholder.com/150/667eea/ffffff?text=BeastX)

**A modern, feature-rich Python library for Telegram**

Inspired by [Telethon](https://github.com/LonamiWebs/Telethon) 💜

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/badge/pypi-beastx--python-orange.svg)](https://pypi.org/project/beastx-python/)

[Documentation](https://beastx.dev/docs) • [Examples](examples/) • [PyPI](https://pypi.org/project/beastx-python/) • [Telegram](https://t.me/GodmrunaL)

**Maintainer:** [@msy1717](https://github.com/msy1717) • **Telegram:** [@GodmrunaL](https://t.me/GodmrunaL)

</div>

---

## ⚠️ Development Status

**BeastX is currently a framework/template** that demonstrates the Telethon-compatible API structure. The library provides:

✅ **Complete API Structure** - Full Telethon-like interface  
✅ **Session Management** - File, String, and Memory sessions  
✅ **Event System Framework** - Event handlers with pattern matching  
✅ **Beautiful Installation** - Animated setup with progress bars  
✅ **Comprehensive Documentation** - Full docs with examples  

✅ **Telethon Included**: BeastX now includes the full Telethon library!

You can use either:
- **BeastX API** - Simple, clean interface
- **Telethon directly** - Full functionality via `from beastx import telethon`

This gives you:
- ✅ Real MTProto connectivity
- ✅ Actual Telegram API functionality  
- ✅ Production-ready messaging
- ✅ File upload/download
- ✅ All Telethon features

📖 **See [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)** for usage examples.

## ✨ Features

- 🚀 **Easy to Use** - Simple, intuitive API similar to Telethon
- 🔄 **Async/Await** - Full async support for modern Python
- 📡 **Event Handlers** - Powerful event system framework
- 💾 **Session Management** - Multiple session types (file, string, memory)
- 🔐 **Secure** - Session storage structure ready for encryption
- 📦 **Auto Dependencies** - Automatically installs required packages
- 🎨 **Beautiful Installation** - Animated installation progress

## 🚀 Quick Start

### Installation

```bash
pip install beastx-python
```

For animated installation with colorful progress:

```bash
pip install beastx-python[animation]
```

### Hello World Bot (Using Telethon)

```python
# Import Telethon through BeastX
from beastx import telethon
from telethon import TelegramClient, events
import asyncio

# Your API credentials from https://my.telegram.org
api_id = 12345
api_hash = 'your_api_hash_here'

# Create client (real Telethon client)
client = TelegramClient('session_name', api_id, api_hash)

# Event handler
@client.on(events.NewMessage(pattern='hello'))
async def handler(event):
    await event.reply('Hi there! 👋 (Real Telethon!)')

# Run the bot
async def main():
    await client.start()
    print("Bot is running with full Telethon functionality!")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
```

## 📖 Documentation

Visit our [comprehensive documentation](https://beastx.dev/docs) for:

- **Getting Started Guide** - Installation and setup
- **User Guide** - Detailed tutorials and examples
- **API Reference** - Complete API documentation
- **Examples** - Ready-to-use code examples

## 🎯 Examples

### Send a Message

```python
from beastx import TelegramClient
import asyncio

async def main():
    client = TelegramClient('sender', api_id, api_hash)
    await client.start()
    
    await client.send_message('@username', 'Hello from BeastX!')
    
    await client.disconnect()

asyncio.run(main())
```

### Echo Bot

```python
@client.on(events.NewMessage)
async def echo(event):
    await event.reply(f"You said: {event.text}")
```

### Pattern Matching

```python
@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.reply("Welcome to BeastX Bot! 🎉")
```

### Get Messages

```python
messages = await client.get_messages('@channel', limit=10)
for msg in messages:
    print(msg.text)
```

More examples in the [examples/](examples/) directory!

## 🛠️ Features in Detail

### Session Types

- **File Session**: Persistent session stored in a file
- **String Session**: Portable session as a string (great for serverless)
- **Memory Session**: Temporary session for testing

### Event System

Support for all Telegram events:

- `NewMessage` - New incoming/outgoing messages
- `MessageEdited` - Edited messages
- `MessageDeleted` - Deleted messages
- `CallbackQuery` - Inline button presses
- `InlineQuery` - Inline queries
- `ChatAction` - User join/leave events
- `UserUpdate` - User status updates

### Client Methods

- `send_message()` - Send text messages
- `get_messages()` - Retrieve messages
- `download_media()` - Download photos/files
- `upload_file()` - Upload files
- `get_entity()` - Get user/chat info
- `get_me()` - Get current user info

## 📦 Dependencies

BeastX automatically installs:

- `requests` - HTTP library
- `flask` - Web framework
- `cryptography` - Encryption
- `pyaes` - AES encryption

## 🙏 Credits

BeastX is **heavily inspired** by [**Telethon**](https://github.com/LonamiWebs/Telethon) by **Lonami Exo**.

We are deeply grateful to the Telethon team for:
- Pioneering the Telegram client library design
- Establishing excellent API patterns
- Creating comprehensive documentation
- Building an amazing open source community

**Thank you, Telethon team! 💜**

## 🤝 Contributing

Contributions are welcome! Please read our guides:

- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute to the project
- **[IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)** - Guide for implementing MTProto using Telethon as reference

Ways to contribute:
- Report bugs and suggest features
- Implement MTProto functionality
- Improve documentation
- Help answer questions

## 📄 License

BeastX is released under the **MIT License**. See [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Documentation**: https://beastx.dev/docs
- **PyPI Package**: https://pypi.org/project/beastx-python/
- **GitHub**: https://github.com/msy1717/beastx-python
- **Issue Tracker**: https://github.com/msy1717/beastx-python/issues
- **Telegram Support**: https://t.me/GodmrunaL
- **Telethon** (Inspiration & Reference): https://github.com/LonamiWebs/Telethon

## 💬 Support

Need help? Check out:

- [Documentation](https://beastx.dev/docs)
- [Examples](examples/)
- [GitHub Issues](https://github.com/msy1717/beastx-python/issues)
- [Telegram](https://t.me/GodmrunaL) - Contact the maintainer
- [Telethon Docs](https://docs.telethon.dev/) - Reference implementation

---

<div align="center">

**Built with ❤️ and gratitude to the open source community**

Special thanks to **Telethon** for showing us the way!

⭐ Star this repo if BeastX helps you! ⭐

</div>
