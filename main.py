import discord
from discord.ext import commands
from discord.ext.commands import errors
import custom_commands

def get_token():  
    f = open('token', 'r')
    return f.readline().rstrip()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_command_error(ctx, error):
    if ctx.invoked_with == 'warn':
        await ctx.send('```Missing argument %s \n'\
             '!warn <user> <time in seconds> <reason>```' % error.param.name)


@bot.command()
async def reset(ctx):    
    await custom_commands.reset(ctx)

@bot.command()
async def clear(ctx):
    await custom_commands.clear_channel(ctx)

@bot.command()
async def warn(ctx, user, time, reason):    
    await custom_commands.warn(ctx, user, time, reason)
          
@bot.command()
async def disconnect(ctx):
    await bot.logout()
    

bot.run(get_token())




