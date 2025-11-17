"""
BeastX Setup Script with Animated Installation

This setup script provides a beautiful animated installation experience
similar to modern CLI tools.
"""
import sys
import time
import subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install

VERSION = '1.0.0'
DESCRIPTION = 'A powerful Telegram client library inspired by Telethon'

LONG_DESCRIPTION = """
# BeastX - Powerful Telegram Client Library

BeastX is a modern, feature-rich Python library for interacting with Telegram's API.
Built with inspiration from Telethon, it provides an intuitive and powerful interface
for building Telegram bots and userbot applications.

## Features

- 🚀 **Easy to Use**: Simple, intuitive API similar to Telethon
- 🔄 **Async/Await**: Full async support for modern Python
- 📡 **Event Handlers**: Powerful event system for handling updates
- 💾 **Session Management**: Multiple session types (file, string, memory)
- 🔐 **Secure**: Built-in encryption and secure session storage
- 📦 **Auto Dependencies**: Automatically installs required packages

## Credits

BeastX is heavily inspired by [Telethon](https://github.com/LonamiWebs/Telethon)
by Lonami Exo. We thank the Telethon team for their excellent work and API design.

## Installation

```bash
pip install beastx-python
```

## Quick Start

```python
from beastx import TelegramClient, events

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(pattern='hello'))
async def handler(event):
    await event.reply('Hi there!')

client.start()
client.run_until_disconnected()
```

For more information, visit our documentation.
"""

DEPENDENCIES = [
    'requests>=2.28.0',
    'flask>=2.3.0',
    'cryptography>=41.0.0',
    'pyaes>=1.6.1',
]


class AnimatedInstallCommand(install):
    """Custom install command with animated progress"""
    
    def run(self):
        """Run installation with beautiful animations"""
        try:
            from colorama import init, Fore, Back, Style
            from tqdm import tqdm
            init(autoreset=True)
            has_animation = True
        except ImportError:
            has_animation = False
            print("\n" + "="*60)
            print("Installing BeastX...")
            print("="*60)
        
        if has_animation:
            self._animated_install()
        
        install.run(self)
        
        if has_animation:
            self._show_completion()
        else:
            print("\n" + "="*60)
            print("✓ BeastX installed successfully!")
            print("="*60 + "\n")
    
    def _animated_install(self):
        """Show animated installation progress"""
        from colorama import Fore, Style
        from tqdm import tqdm
        
        banner = f"""
{Fore.CYAN}{'='*60}
{Fore.YELLOW}    ____                  __   __  __
{Fore.YELLOW}   / __ )___  ____ ______/ /_ / / / /
{Fore.YELLOW}  / __  / _ \\/ __ `/ ___/ __// /_/ / 
{Fore.YELLOW} / /_/ /  __/ /_/ (__  ) /_ / __  /  
{Fore.YELLOW}/_____/\\___/\\__,_/____/\\__//_/ /_/   
{Fore.CYAN}
{Fore.GREEN}  Powerful Telegram Client Library
{Fore.MAGENTA}  Inspired by Telethon
{Fore.CYAN}{'='*60}{Style.RESET_ALL}
"""
        print(banner)
        
        steps = [
            "Setting up package structure",
            "Installing core dependencies",
            "Configuring session management",
            "Setting up event handlers",
            "Initializing client modules",
            "Finalizing installation"
        ]
        
        for step in tqdm(steps, desc=f"{Fore.CYAN}Installing BeastX", 
                        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}",
                        colour='green'):
            time.sleep(0.3)
    
    def _show_completion(self):
        """Show installation completion message"""
        from colorama import Fore, Style
        
        completion_msg = f"""
{Fore.GREEN}{'='*60}
{Fore.GREEN}✓ Installation Complete!{Style.RESET_ALL}

{Fore.CYAN}Getting Started:{Style.RESET_ALL}
  {Fore.WHITE}from beastx import TelegramClient, events{Style.RESET_ALL}

{Fore.CYAN}Documentation:{Style.RESET_ALL}
  {Fore.WHITE}Check the docs/ folder for complete guides{Style.RESET_ALL}

{Fore.YELLOW}Credits:{Style.RESET_ALL}
  {Fore.WHITE}Special thanks to Telethon by Lonami Exo{Style.RESET_ALL}
  {Fore.WHITE}https://github.com/LonamiWebs/Telethon{Style.RESET_ALL}

{Fore.GREEN}{'='*60}{Style.RESET_ALL}
"""
        print(completion_msg)


setup(
    name='beastx-python',
    version=VERSION,
    author='BeastX Team',
    author_email='info@beastx.dev',
    maintainer='GodmrunaL',
    maintainer_email='godmrunal@beastx.dev',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/msy1717/beastx-python',
    packages=find_packages(include=['beastx', 'beastx.*', 'telethon', 'telethon.*']),
    install_requires=DEPENDENCIES,
    extras_require={
        'animation': ['tqdm>=4.65.0', 'colorama>=0.4.6'],
        'dev': ['pytest>=7.0.0', 'pytest-asyncio>=0.21.0', 'black>=23.0.0'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat',
    ],
    python_requires='>=3.8',
    keywords='telegram, telegram-client, telegram-bot, telethon, mtproto, api',
    cmdclass={
        'install': AnimatedInstallCommand,
    },
    project_urls={
        'Documentation': 'https://msy1717.github.io/beastx-python',
        'Source': 'https://github.com/msy1717/beastx-python',
        'Tracker': 'https://github.com/msy1717/beastx-python/issues',
        'Telegram': 'https://t.me/GodmrunaL',
        'Telethon': 'https://github.com/LonamiWebs/Telethon',
    },
)
