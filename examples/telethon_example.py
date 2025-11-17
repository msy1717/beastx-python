"""
Using Telethon directly through BeastX

This example shows how to use the included Telethon library
for real Telegram functionality.
"""

# Import Telethon through BeastX
from beastx import telethon
from telethon import TelegramClient, events
import asyncio

# Your API credentials from https://my.telegram.org
API_ID = 12345
API_HASH = 'your_api_hash_here'
BOT_TOKEN = 'your_bot_token_here'

# Create Telethon client
client = TelegramClient('telethon_session', API_ID, API_HASH)


@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    """Handle /start command with real Telethon"""
    await event.reply(
        '👋 **Welcome!**\n\n'
        'This bot uses Telethon included in BeastX!\n'
        'Full MTProto connectivity and all features! 🚀'
    )


@client.on(events.NewMessage(pattern='/help'))
async def help_handler(event):
    """Handle /help command"""
    await event.reply(
        '**BeastX + Telethon Bot**\n\n'
        'Commands:\n'
        '/start - Start the bot\n'
        '/help - Show this message\n'
        '/ping - Check if bot is alive\n\n'
        'Powered by Telethon through BeastX!'
    )


@client.on(events.NewMessage(pattern='/ping'))
async def ping_handler(event):
    """Handle /ping command"""
    await event.reply('🏓 Pong! Using real Telethon!')


async def main():
    """Start the bot with real Telethon"""
    print("Starting bot with Telethon...")
    
    # Start with bot token
    await client.start(bot_token=BOT_TOKEN)
    
    me = await client.get_me()
    print(f"Bot started: @{me.username}")
    print("Bot is running with full Telethon functionality!")
    
    # Run until disconnected
    await client.run_until_disconnected()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot stopped.")
