# Authentication

BeastX supports multiple authentication methods for both bots and user accounts.

## Bot Authentication

Authenticate as a bot using a bot token from [@BotFather](https://t.me/botfather):

```python
from beastx import TelegramClient
import asyncio

client = TelegramClient('bot_session', api_id, api_hash)

async def main():
    # Start with bot token
    await client.start(bot_token='123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11')
    
    # Get bot info
    me = await client.get_me()
    print(f"Logged in as {me['username']}")
    
    await client.run_until_disconnected()

asyncio.run(main())
```

## User Authentication

Authenticate as a user with your phone number:

```python
async def main():
    # Start with phone number
    await client.start(phone='+1234567890')
    
    # You'll be prompted for:
    # 1. Verification code (sent via SMS or Telegram)
    # 2. 2FA password (if enabled)
    
    me = await client.get_me()
    print(f"Logged in as {me['phone']}")
    
    await client.run_until_disconnected()

asyncio.run(main())
```

## Programmatic Authentication

Handle authentication in code without user input:

```python
async def main():
    await client.start(
        phone=lambda: input('Phone: '),
        password=lambda: input('2FA password: '),
        code_callback=lambda: input('Code: ')
    )
    
    await client.run_until_disconnected()

asyncio.run(main())
```

## Session Types

### File Session (Default)

Stores session data in a file:

```python
from beastx import TelegramClient, Session

session = Session('my_account')
client = TelegramClient(session, api_id, api_hash)
```

### String Session

Stores session as a portable string (useful for serverless):

```python
from beastx import TelegramClient, StringSession

# Create new session
session = StringSession()
client = TelegramClient(session, api_id, api_hash)

await client.start()
session_string = session.save()
print(f"Save this: {session_string}")

# Later, restore from string
restored_session = StringSession(session_string)
client = TelegramClient(restored_session, api_id, api_hash)
```

### Memory Session

Temporary session that doesn't persist:

```python
from beastx import TelegramClient, MemorySession

session = MemorySession()
client = TelegramClient(session, api_id, api_hash)

# Session is lost when program exits
```

## Environment Variables

Store credentials securely using environment variables:

```python
import os
from beastx import TelegramClient

api_id = int(os.getenv('TELEGRAM_API_ID'))
api_hash = os.getenv('TELEGRAM_API_HASH')
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

client = TelegramClient('bot', api_id, api_hash)
await client.start(bot_token=bot_token)
```

## Best Practices

!!! warning "Security"
    - Never commit session files or API credentials to version control
    - Use environment variables for sensitive data
    - Keep your `api_hash` and bot tokens secret
    - Don't share session strings - they grant full account access

!!! tip "Sessions"
    - Use StringSession for serverless/cloud deployments
    - Use MemorySession for testing
    - Use File Session for local development and production servers

## Session Management

### Deleting Sessions

```python
# Delete session file
session = Session('my_account')
session.delete()

# Clear string session
string_session = StringSession(session_string)
string_session.delete()
```

### Checking Session Status

```python
session = Session('my_account')
dc_id, server, port = session.get_dc()

if dc_id:
    print(f"Connected to DC {dc_id}")
else:
    print("Not authenticated")
```

## Next Steps

- Learn about [Sending Messages](../guide/sending-messages.md)
- Explore [Event Handlers](../guide/events.md)
- Check out [Session Details](../guide/sessions.md)
