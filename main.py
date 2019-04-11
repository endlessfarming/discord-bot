import discord
import commands

token = 'NTY1ODgxMjMwNDIwMjEzNzg1.XK8-pg.oeI4b3F377zZRf240WndmM-PbgE'

client = discord.Client()

@client.event
async def on_message(message):
    await commands.parse(message)





client.run(token)




