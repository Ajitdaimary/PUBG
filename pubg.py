import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import requests
import json
import aiohttp

client = commands.Bot(description="Here is some command for you", command_prefix=commands.when_mentioned_or("p!"), pm_help = False)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+'')
	print('--------')
	print('--------')
	print('Started pubg') #add_your_bot_name_here
	return await client.change_presence(game=discord.Game(name='bc players')) #add_your_bot_status_here

@client.command(pass_context=True)
async def tweet(ctx, usernamename:str, *, txt:str):
    url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={usernamename}&text={txt}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_image(url=res['message'])
            embed.title = "{} twitted: {}".format(usernamename, txt)
            await client.say(embed=embed)

		
@client.command(pass_context = True)
async def invites(ctx,*,user:discord.Member=None):
    invite = await client.invites_from(ctx.message.server)
    if user is None:
        for invite in invite:
          if invite.inviter == ctx.message.author:
              r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
              embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
              embed.add_field(name = 'Link used for inviting:',value =f'{invite.url}'.format(), inline=False)
              embed.add_field(name = 'Invites from this link:',value =f'{invite.uses}', inline=False)
              embed.add_field(name = 'Created at:',value =f'{invite.created_at}', inline=False)
              embed.add_field(name = 'Channel:',value =f'{invite.channel}', inline=False)
              embed.add_field(name = 'ID:',value =f'{invite.id}', inline=False)
              await client.say(embed=embed)
    
   else:
        for invite in invite:
          if invite.inviter == user:
              r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
              embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
              embed.add_field(name = 'Link used for inviting:',value =f'{invite.url}'.format(), inline=False)
              embed.add_field(name = 'Invites from this link:',value =f'{invite.uses}', inline=False)
              embed.add_field(name = 'Created at:',value =f'{invite.created_at}', inline=False)
              embed.add_field(name = 'Channel:',value =f'{invite.channel}', inline=False)
              embed.add_field(name = 'ID:',value =f'{invite.id}', inline=False)
              await client.say(embed=embed)
		
client.run(os.getenv('Token'))
