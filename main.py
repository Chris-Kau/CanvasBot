# pip install python-dotenv
# pip install discord
import os
from dotenv import load_dotenv
import discord
from discord import Intents, Client, Message
from discord.ext import commands, tasks
import responses
import datetime
from timeconverter import time_to_word
from classassignments import get_assignment_list


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)
#basic message response

#startup message
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running")
    #create default files
    file = open("token_state.txt", "w")
    file.write('0')
    file.close()
    file = open("user_token.txt", "w")
    file.write('NULL')
    file.close()

async def send_message(message, user_message):
    if not user_message:
        return
    if user_message[0] == '!':
        user_message = user_message[1:]
        try:
            response = responses.get_response(user_message)
            if "todo" in user_message.lower() and open("token_state.txt").read() == "1":
                embed = discord.Embed(title="To-Do List", description=response[0], color=discord.Color.purple())
                embed.set_footer(text=response[1])
                await message.channel.send(embed=embed)
            else:
                await message.channel.send(response)
        except Exception as e:
            print(e)
    elif user_message == '?reminder' and open("token_state.txt").read() == "1":
        reminder.start(message)
    else:
        await message.channel.send(responses.get_response(user_message))


#handle incoming messages (so bot doesnt read its own message)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    user_message = str(message.content)
    await send_message(message, user_message)


@tasks.loop(seconds=5) #hours=24
async def reminder(message):
    next_three_day = datetime.date.today() + datetime.timedelta(days=3)
    output_string = ''
    #go to responses.py then go to todo.py and grab assignment list
    assignments_list = get_assignment_list()
    for i in assignments_list:
        due_date = i.rsplit(' ', 2)
        if "Date" in due_date[2]: #When there is not due date
            continue

        year, month, day = due_date[1].split('|')[1].split('-')
        type_date = datetime.date(int(year), int(month), int(day))
        if type_date <= next_three_day:
            output_string += f"*{time_to_word(str(due_date[1].split('|')[1] + ' ' +  due_date[2]))}* - {due_date[0][6:]} \n"
    embed = discord.Embed(title="DUE WITHIN 3 DAYS", description=output_string, color=discord.Color.purple())
    await message.author.send(embed=embed)
        

def main():
    client.run(token=TOKEN)
    


if __name__ == '__main__':
    main()