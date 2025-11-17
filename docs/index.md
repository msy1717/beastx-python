# Welcome to BeastX

<div class="hero-section">
  <h1 class="hero-title">⚡ BeastX</h1>
  <p class="hero-subtitle">A Powerful Telegram Client Library for Python</p>
</div>

## What is BeastX?

BeastX is a modern, feature-rich Python library for interacting with Telegram's API. Built with inspiration from **Telethon**, it provides an intuitive and powerful interface for building Telegram bots and userbot applications.

## ✨ Key Features

- **🚀 Easy to Use** - Simple, intuitive API similar to Telethon
- **🔄 Async/Await** - Full async support for modern Python applications
- **📡 Event Handlers** - Powerful event system for handling updates
- **💾 Session Management** - Multiple session types (file, string, memory)
- **🔐 Secure** - Built-in encryption and secure session storage
- **📦 Auto Dependencies** - Automatically installs required packages
- **🎨 Beautiful Installation** - Animated installation progress with colorful output

## Quick Example

```python
from beastx import TelegramClient, events

# Initialize the client
client = TelegramClient('session_name', api_id, api_hash)

# Register an event handler
@client.on(events.NewMessage(pattern='hello'))
async def handler(event):
    await event.reply('Hi there! 👋')

# Start the client
async def main():
    await client.start()
    await client.run_until_disconnected()

import asyncio
asyncio.run(main())
```

## Installation

Install BeastX using pip:

```bash
pip install beastx-python
```

For development installation with animation support:

```bash
pip install beastx-python[animation]
```

## Why BeastX?

BeastX combines the best practices from Telethon with modern Python features:

- **Familiar API** - If you know Telethon, you know BeastX
- **Well Documented** - Comprehensive docs with examples
- **Active Development** - Regular updates and improvements
- **Community Driven** - Open source and welcoming contributions

## Credits & Acknowledgments

!!! info "Built on Giants' Shoulders"
    BeastX is heavily inspired by [**Telethon**](https://github.com/LonamiWebs/Telethon) by Lonami Exo.
    We are grateful for the excellent API design and patterns established by the Telethon team.
    
    **Thank you, Telethon team, for pioneering this API design! 🙏**

## Get Started

Ready to build your Telegram application? Check out our [Quick Start Guide](getting-started/quickstart.md) to get up and running in minutes!

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with BeastX in under 5 minutes

    [:octicons-arrow-right-24: Getting Started](getting-started/quickstart.md)

-   :material-book-open-variant:{ .lg .middle } __API Reference__

    ---

    Complete API documentation for all classes and methods

    [:octicons-arrow-right-24: API Docs](api/client.md)

-   :material-code-braces:{ .lg .middle } __Examples__

    ---

    Learn from practical examples and use cases

    [:octicons-arrow-right-24: View Examples](examples/basic-bot.md)

-   :material-github:{ .lg .middle } __Source Code__

    ---

    Check out the source code on GitHub

    [:octicons-arrow-right-24: GitHub](https://github.com/msy1717/beastx-python)

</div>

## 📞 Contact & Support

- **Maintainer**: [@msy1717](https://github.com/msy1717) on GitHub
- **Telegram**: [@GodmrunaL](https://t.me/GodmrunaL)
- **Reference**: See [Telethon](https://github.com/LonamiWebs/Telethon) for full implementation
