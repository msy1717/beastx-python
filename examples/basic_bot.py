"""
Basic Bot Example - Simple Telegram bot with BeastX

This example shows how to create a basic bot that responds to commands.
"""

from beastx import TelegramClient, events
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

API_ID = 12345
API_HASH = 'your_api_hash_here'
BOT_TOKEN = 'your_bot_token_here'

client = TelegramClient('bot_session', API_ID, API_HASH)


@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    """Handle /start command"""
    await event.reply(
        "👋 **Welcome to BeastX Bot!**\n\n"
        "I'm a bot built with BeastX library.\n\n"
        "**Commands:**\n"
        "/help - Show help message\n"
        "/about - About this bot\n"
        "/ping - Check if bot is alive"
    )


@client.on(events.NewMessage(pattern='/help'))
async def help_handler(event):
    """Handle /help command"""
    await event.reply(
        "**BeastX Bot Help**\n\n"
        "This bot demonstrates BeastX capabilities:\n"
        "• Message handling\n"
        "• Event system\n"
        "• Pattern matching\n\n"
        "Visit https://beastx.dev for documentation!"
    )


@client.on(events.NewMessage(pattern='/about'))
async def about_handler(event):
    """Handle /about command"""
    await event.reply(
        "**About BeastX Bot**\n\n"
        "Built with: BeastX v1.0.0\n"
        "Inspired by: Telethon\n\n"
        "BeastX is a powerful Telegram client library!\n"
        "Credits to Telethon for the amazing API design. 💜"
    )


@client.on(events.NewMessage(pattern='/ping'))
async def ping_handler(event):
    """Handle /ping command"""
    await event.reply("🏓 Pong! Bot is alive and running.")


async def main():
    """Main function to start the bot"""
    print("Starting BeastX Bot...")
    
    await client.start(bot_token=BOT_TOKEN)
    
    me = await client.get_me()
    print(f"Bot started as @{me.get('username', 'unknown')}")
    print("Bot is running. Press Ctrl+C to stop.")
    
    await client.run_until_disconnected()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot stopped by user.")
