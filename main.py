import discord
import commands


def get_token():  
    f = open('token', 'r')
    return f.readline().rstrip()

client = discord.Client()

@client.event
async def on_message(message):
    await commands.parse(message)





client.run(get_token())




