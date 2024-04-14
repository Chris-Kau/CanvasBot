# pip install python-dotenv
# pip install discord
import os
from dotenv import load_dotenv
import discord
from discord import Intents, Client, Message
from discord.ext import commands, tasks
import responses
import datetime


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = Intents.default()
intents.message_content = True
# bot = commands.Bot(command_prefix='+', help_command=None, intents=intents)
client = Client(intents=intents)
#basic message response

checked = 0

#startup message
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running")

async def send_message(message, user_message):
    # embed=discord.Embed(title="To-Do List", description="This is an embed that will show how to build an embed and the different components", color=discord.Color.blue())
    # embed.set_footer(text="This is the footer. It contains text at the bottom of the embed")    
    # await message.channel.send(embed=embed)
    
    if not user_message:
        return
    if user_message[0] == '!':
        user_message = user_message[1:]
    elif user_message == '?reminder':
        reminder.start(message)
    try:
        response = responses.get_response(user_message)
        if "todo" in user_message.lower():
            embed = discord.Embed(title="To-Do List", description=response[0], color=discord.Color.purple())
            embed.set_footer(text=response[1])
            await message.channel.send(embed=embed)
        else:
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
    # await bot.process_commands(message)

    # username = str(message.author)
    user_message = str(message.content)
    # channel = str(message.channel)
    # print(f"{channel} {username} {user_message}")
    await send_message(message, user_message)


@tasks.loop(seconds=5) #hours=24
async def reminder(message):
    next_three_day = datetime.date.today() + datetime.timedelta(days=3)
    output_string = ''
    #go to responses.py then go to todo.py and grab assignment list
    for i in responses.todo.assignment_list:
        due_date = i.rsplit(' ', 2)[1]
        if due_date == 'due': #When there is not due date
            continue
        year, month, day = due_date.split('-')
        type_date = datetime.date(int(year), int(month), int(day))
        if type_date <= next_three_day:
            output_string += i + '\n'
    await message.author.send(output_string)
        

def main():
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()