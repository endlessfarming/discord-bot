import discord
from discord.ext import commands
import custom_commands

def get_token():  
    f = open('token', 'r')
    return f.readline().rstrip()

bot = commands.Bot(command_prefix='!')

@bot.command()
async def reset(ctx):    
    await custom_commands.reset(ctx)

@bot.command()
async def clear(ctx):
    await custom_commands.clear_channel(ctx)


bot.run(get_token())




