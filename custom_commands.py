from discord import utils
import asyncio
import time_helper

async def clear_channel(ctx):   
    if (ctx.author.guild_permissions.manage_messages): 
        msgs = []
        async for message in ctx.channel.history():
            msgs.append(message)
        
        await ctx.channel.delete_messages(msgs)

async def reset(ctx):
    await ctx.send(time_helper.get_reset())

async def warn(ctx, user, time, reason):    
    member = utils.find(lambda m: m.mention == user, ctx.channel.guild.members)
    role = utils.get(ctx.author.guild.roles, name='Muted')
    if (member is None):
        await ctx.send('```User %s not found.```' % user)
    else:
        await member.add_roles(role, reason=reason)
        await ctx.send('```User %s has been muted for %s seconds, reason = %s ```'
        % (member.name, time, reason))
        await asyncio.sleep(int(time))
        await member.remove_roles(role, reason='timed out')

    