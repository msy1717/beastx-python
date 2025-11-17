# Quick Start

Get started with BeastX in just a few minutes!

## Prerequisites

Before you begin, you'll need:

1. **Python 3.8+** installed on your system
2. **Telegram API credentials** (API ID and API Hash)

## Getting API Credentials

1. Visit [https://my.telegram.org](https://my.telegram.org)
2. Log in with your phone number
3. Go to "API Development Tools"
4. Create a new application
5. Note down your `api_id` and `api_hash`

## Your First Bot

Here's a simple echo bot that replies to every message:

```python
from beastx import TelegramClient, events
import asyncio

# Your API credentials
api_id = 12345
api_hash = 'your_api_hash_here'

# Create the client
client = TelegramClient('my_bot', api_id, api_hash)

# Event handler for new messages
@client.on(events.NewMessage)
async def echo_handler(event):
    """Echo back any message received"""
    await event.reply(f"You said: {event.text}")

# Main function
async def main():
    # Start the client (you'll be prompted for phone/bot token)
    await client.start()
    print("Bot is running...")
    
    # Run until disconnected
    await client.run_until_disconnected()

# Run the bot
if __name__ == '__main__':
    asyncio.run(main())
```

## Bot with Pattern Matching

Make your bot respond to specific commands:

```python
from beastx import TelegramClient, events
import asyncio

client = TelegramClient('smart_bot', api_id, api_hash)

@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.reply(
        "👋 Welcome to BeastX Bot!\n\n"
        "Commands:\n"
        "/help - Show this message\n"
        "/about - About this bot"
    )

@client.on(events.NewMessage(pattern='/help'))
async def help_handler(event):
    await event.reply("Need help? Contact @support")

@client.on(events.NewMessage(pattern='(?i)hello'))
async def hello_handler(event):
    await event.reply("Hi there! 👋")

async def main():
    await client.start()
    print("Smart bot is running!")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
```

## Sending Messages

Send messages to users or channels:

```python
from beastx import TelegramClient
import asyncio

client = TelegramClient('sender', api_id, api_hash)

async def main():
    await client.start()
    
    # Send to a username
    await client.send_message('@username', 'Hello!')
    
    # Send to a chat ID
    await client.send_message(123456789, 'Hi there!')
    
    # Send with formatting
    await client.send_message(
        '@username',
        '**Bold text** and *italic text*',
        parse_mode='markdown'
    )
    
    await client.disconnect()

asyncio.run(main())
```

## Getting Messages

Retrieve messages from a chat:

```python
async def main():
    await client.start()
    
    # Get last 10 messages
    messages = await client.get_messages('@channel', limit=10)
    
    for msg in messages:
        print(f"{msg.sender_id}: {msg.text}")
    
    await client.disconnect()

asyncio.run(main())
```

## Using Context Manager

Use the `async with` statement for automatic connection management:

```python
async def main():
    async with TelegramClient('session', api_id, api_hash) as client:
        await client.send_message('me', 'Hello from BeastX!')
        # Client automatically disconnects when exiting the context

asyncio.run(main())
```

## What's Next?

- Learn about [Authentication](authentication.md) options
- Explore [Event Handlers](../guide/events.md) in depth
- Check out [Complete Examples](../examples/basic-bot.md)
- Read the [API Reference](../api/client.md)

!!! tip "Pro Tip"
    Always use async/await when working with BeastX. All client methods are asynchronous!
