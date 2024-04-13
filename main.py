import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)
#basic message response
async def send_message(message, user_message):
    if not user_message:
        return
    if is_private := user_message[0] == '!':
        user_message = user_message[1:]
    try:
        response: str = get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

#startup message
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running")

#handle incoming messages (so bot doesnt read its own message)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    print(f"{channel} {username} {user_message}")
    await send_message(message, user_message)

def main():
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()