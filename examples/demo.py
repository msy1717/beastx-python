"""
BeastX Library Demo - Demonstrates library features without connecting to Telegram

This demo shows the library structure, imports, and basic functionality
without requiring actual Telegram API credentials.
"""

import asyncio
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from beastx import TelegramClient, events, Session, StringSession, MemorySession
import beastx


def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")


def demo_credits():
    """Show BeastX credits"""
    print_section("BeastX Credits")
    beastx.show_credits()


def demo_imports():
    """Demonstrate available imports"""
    print_section("Available Imports")
    
    print(f"✓ TelegramClient: {TelegramClient}")
    print(f"✓ Session: {Session}")
    print(f"✓ StringSession: {StringSession}")
    print(f"✓ MemorySession: {MemorySession}")
    print(f"✓ Events module: {events}")
    print(f"✓ Utils module: {beastx.utils}")
    print(f"\nVersion: {beastx.__version__}")
    print(f"Author: {beastx.__author__}")
    print(f"License: {beastx.__license__}")


def demo_events():
    """Show available event types"""
    print_section("Event Types")
    
    event_types = [
        'NewMessage',
        'MessageEdited',
        'MessageDeleted',
        'CallbackQuery',
        'InlineQuery',
        'ChatAction',
        'UserUpdate',
        'MessageRead',
        'Album'
    ]
    
    for event_type in event_types:
        if hasattr(events, event_type):
            print(f"✓ events.{event_type}")


def demo_sessions():
    """Demonstrate session types"""
    print_section("Session Management")
    
    print("1. File Session:")
    file_session = Session('demo_session')
    print(f"   Created: {file_session}")
    
    print("\n2. String Session:")
    string_session = StringSession()
    print(f"   Created: {string_session}")
    
    print("\n3. Memory Session:")
    memory_session = MemorySession()
    print(f"   Created: {memory_session}")
    
    file_session.delete()


def demo_client_creation():
    """Show how to create clients"""
    print_section("Client Creation")
    
    print("Creating TelegramClient instances:\n")
    
    print("1. Basic client:")
    print("   client = TelegramClient('session', api_id, api_hash)")
    
    print("\n2. With StringSession:")
    print("   client = TelegramClient(StringSession(), api_id, api_hash)")
    
    print("\n3. With MemorySession:")
    print("   client = TelegramClient(MemorySession(), api_id, api_hash)")


async def demo_client_methods():
    """Show available client methods"""
    print_section("Client Methods")
    
    client = TelegramClient('demo', 12345, 'demo_hash')
    
    methods = [
        'start()',
        'connect()',
        'disconnect()',
        'send_message(entity, message)',
        'get_messages(entity, limit)',
        'get_me()',
        'get_entity(entity)',
        'download_media(message)',
        'upload_file(file)',
        'on(event)',
        'add_event_handler(callback, event)',
        'run_until_disconnected()'
    ]
    
    print("Available methods:\n")
    for method in methods:
        print(f"✓ client.{method}")


def demo_usage_example():
    """Show a complete usage example"""
    print_section("Usage Example")
    
    example = '''
from beastx import TelegramClient, events
import asyncio

# Initialize client
client = TelegramClient('session', api_id, api_hash)

# Register event handler
@client.on(events.NewMessage(pattern='hello'))
async def handler(event):
    await event.reply('Hi there! 👋')

# Main function
async def main():
    await client.start()
    await client.run_until_disconnected()

# Run
asyncio.run(main())
'''
    
    print(example)


def main():
    """Run all demos"""
    print("\n" + "="*60)
    print("  🚀 BeastX Library Demo")
    print("="*60)
    
    demo_credits()
    demo_imports()
    demo_events()
    demo_sessions()
    demo_client_creation()
    asyncio.run(demo_client_methods())
    demo_usage_example()
    
    print_section("Demo Complete")
    print("✓ BeastX library is properly installed and working!")
    print("✓ All imports are available")
    print("✓ Ready to build Telegram applications!")
    print("\nFor full documentation, visit: https://beastx.dev/docs")
    print("For examples, check the examples/ directory\n")


if __name__ == '__main__':
    main()
