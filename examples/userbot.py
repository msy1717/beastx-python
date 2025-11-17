"""
Userbot Example - User account automation

This example shows how to use BeastX with a user account.
WARNING: Use responsibly and comply with Telegram's ToS!
"""

from beastx import TelegramClient, events
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

API_ID = 12345
API_HASH = 'your_api_hash_here'

client = TelegramClient('userbot_session', API_ID, API_HASH)


@client.on(events.NewMessage(outgoing=True, pattern=r'\.ping'))
async def ping_command(event):
    """Respond to .ping command"""
    await event.edit("🏓 Pong!")


@client.on(events.NewMessage(outgoing=True, pattern=r'\.info'))
async def info_command(event):
    """Show account info"""
    me = await client.get_me()
    await event.edit(
        f"**Account Info:**\n"
        f"ID: {me.get('id')}\n"
        f"Phone: {me.get('phone', 'N/A')}\n"
        f"Is Bot: {me.get('is_bot', False)}"
    )


@client.on(events.NewMessage(incoming=True, pattern='hello'))
async def auto_reply(event):
    """Auto-reply to hello messages"""
    await event.reply("Hi! This is an automated response from BeastX userbot.")


async def main():
    """Start the userbot"""
    print("Starting Userbot...")
    
    await client.start()
    
    me = await client.get_me()
    print(f"Userbot started for: {me.get('phone', 'Unknown')}")
    print("Userbot is running. Use .ping or .info commands.")
    
    await client.run_until_disconnected()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nUserbot stopped.")
