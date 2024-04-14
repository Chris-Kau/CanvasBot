# pip install python-dotenv
# pip install discord
import json
import os
from dotenv import load_dotenv
import discord
from discord import Intents, Client, Message
from discord.ext import commands, tasks
import responses
import datetime
from timeconverter import time_to_word
from classassignments import get_assignment_list
import copy
import requests

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TENOR_KEY = os.getenv('TENOR_KEY')
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
    if user_message == '!reminder' and open("token_state.txt").read() == "1":
        reminder.start(message)
    elif user_message[0] == '!':
        user_message = user_message[1:]
        try:
            response = responses.get_response(user_message)
            if "todo" in user_message.lower() and open("token_state.txt").read() == "1":
                embed = discord.Embed(title="To-Do List", description=response[0], color=discord.Color.purple())
                embed.set_footer(text=response[1])
                await message.channel.send(embed=embed)
            elif "help" == user_message.lower():
                helpembed = discord.Embed(title = "List of Commands", description=response, color = discord.Color.purple())
                helpembed.set_footer(text="NOTE: !settoken is **REQUIRED** to access other commands apart from !help and !guide... and !cats")
                await message.channel.send(embed=helpembed)
            elif "guide" == user_message.lower():
                guideembed = discord.Embed(title = "How To Get Your Access Token", description=response, color = discord.Color.purple())
                image1 = discord.Embed()
                image2 = discord.Embed()
                image3 = discord.Embed()
                image1.set_image(url='https://cdn.discordapp.com/attachments/1099064514298781748/1229024485269835836/image.png?ex=662e2d3f&is=661bb83f&hm=b50bf6a0a88dcbc3b9a980ffca8ccb374590e869d40c3a698352e8e1d196fa4d&')
                image2.set_image(url='https://cdn.discordapp.com/attachments/1099064514298781748/1229025286994006026/image.png?ex=662e2dfe&is=661bb8fe&hm=845ba018b8ac97a1e1f870422407cf236dce492faeeb733bd412e1005db5cd49&')
                image3.set_image(url='https://cdn.discordapp.com/attachments/1099064514298781748/1229025574979375144/image.png?ex=662e2e43&is=661bb943&hm=6363fa3214fef6812a063ecd28a72add8a73c955bc28d8efd1d62a8b2fdb641b&')
                await message.channel.send(embeds = [guideembed, image1, image2, image3])
            elif "cats" == user_message.lower():
                r = requests.get('https://api.thecatapi.com/v1/images/search?format=json&mime_types=gif')
                cats = json.loads(r.text)
                await message.channel.send(cats[0]['url'])
            else:
                await message.channel.send(response)
        except Exception as e:
            print(e)



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
    assignments_list = copy.copy(list(get_assignment_list()))
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