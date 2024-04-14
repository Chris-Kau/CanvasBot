# pip install python-dotenv
# pip install discord
import os
from dotenv import load_dotenv
import discord
from discord import Intents, Client, Message
from discord.ext import commands, tasks
import responses


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = Intents.default()
intents.message_content = True
# bot = commands.Bot(command_prefix='+', help_command=None, intents=intents)
client = Client(intents=intents)
#basic message response

checked = 0
todo_list = []
#startup message
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running")


async def send_message(message, user_message):
    embed=discord.Embed(title="Sample Embed", description="This is an embed that will show how to build an embed and the different components", color=discord.Color.blue())
    embed.set_footer(text="This is the footer. It contains text at the bottom of the embed")    
    await message.channel.send(embed=embed)
    
    if not user_message:
        return
    if user_message[0] == '!':
        user_message = user_message[1:]
    elif user_message == '?reminder':
        reminder.start(message)
    try:
        response: str = responses.get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

    
        

#handle incoming messages (so bot doesnt read its own message)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # await bot.process_commands(message)

    # username = str(message.author)
    user_message = str(message.content)
    # channel = str(message.channel)
    # print(f"{channel} {username} {user_message}")
    await send_message(message, user_message)


@tasks.loop(seconds=2)
async def reminder(message):
    await message.author.send('You will now receive reminders every 24 hours')


def main():
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()