"""
Echo Bot Example - Bot that echoes back every message

This example demonstrates event handlers and message replies.
"""

from beastx import TelegramClient, events
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

API_ID = 12345
API_HASH = 'your_api_hash_here'
BOT_TOKEN = 'your_bot_token_here'

client = TelegramClient('echo_bot', API_ID, API_HASH)


@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    """Welcome message"""
    await event.reply(
        "👋 Hello! I'm an Echo Bot!\n\n"
        "Send me any message and I'll echo it back to you.\n"
        "Built with BeastX library. 🚀"
    )


@client.on(events.NewMessage)
async def echo_handler(event):
    """Echo back any message"""
    if event.text and not event.text.startswith('/'):
        await event.reply(f"🔊 You said: {event.text}")


async def main():
    """Start the echo bot"""
    print("Starting Echo Bot...")
    
    await client.start(bot_token=BOT_TOKEN)
    
    print("Echo Bot is running!")
    print("Send messages to see them echoed back.")
    
    await client.run_until_disconnected()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nEcho Bot stopped.")
