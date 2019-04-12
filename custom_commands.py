from datetime import datetime, timedelta
from discord import utils

async def clear_channel(ctx):   
    if (ctx.author.guild_permissions.manage_messages): 
        msgs = []
        async for message in ctx.channel.history():
            msgs.append(message)
        
        await ctx.channel.delete_messages(msgs)

async def reset(ctx):
    utc_now = datetime.utcnow()
    utc_reset = utc_now.replace(hour=0, minute=0, second=0, microsecond=0)
    td = timedelta(seconds=(utc_reset-utc_now).seconds)
    td_str = str(td).split(':')
    await ctx.send('```%s hours, %s minutes, %s seconds until reset```' %  (td_str[0], td_str[1], td_str[2]))

