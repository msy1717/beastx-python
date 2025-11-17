# 🚀 Quick Start Guide

## BeastX now includes Telethon!

You get **full Telegram functionality** out of the box!

## Installation

```bash
pip install beastx-python
```

## Using Telethon Through BeastX

### Option 1: Import Telethon Directly

```python
from beastx import telethon
from telethon import TelegramClient, events

# Use Telethon as normal!
client = TelegramClient('session', api_id, api_hash)
```

### Option 2: Full Import

```python
from beastx.telethon import TelegramClient, events

# Same as above, shorter import
client = TelegramClient('session', api_id, api_hash)
```

## Complete Working Example

```python
from beastx import telethon
from telethon import TelegramClient, events
import asyncio

# Get these from https://my.telegram.org
API_ID = 12345
API_HASH = 'your_api_hash'
BOT_TOKEN = 'your_bot_token'

client = TelegramClient('bot_session', API_ID, API_HASH)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply('🎉 BeastX + Telethon working!')

async def main():
    await client.start(bot_token=BOT_TOKEN)
    print("Bot is running!")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
```

## What You Get

✅ **Full MTProto Implementation** - Real Telegram connectivity  
✅ **All Telethon Features** - Messages, files, channels, everything!  
✅ **Production Ready** - Battle-tested code from Telethon  
✅ **BeastX Simplicity** - Easy import and setup  
✅ **No Extra Dependencies** - Telethon included!

## Documentation

- **BeastX Docs**: https://msy1717.github.io/beastx-python
- **Telethon Docs**: https://docs.telethon.dev
- **Examples**: Check `examples/` folder

## Get API Credentials

1. Visit https://my.telegram.org
2. Login with your phone
3. Go to "API Development Tools"
4. Create an application
5. Get your `api_id` and `api_hash`

## Support

- **Telegram**: [@GodmrunaL](https://t.me/GodmrunaL)
- **GitHub**: [msy1717/beastx-python](https://github.com/msy1717/beastx-python)
- **Issues**: [Report here](https://github.com/msy1717/beastx-python/issues)

---

**Powered by Telethon** 💜
