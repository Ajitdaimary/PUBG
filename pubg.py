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


client = commands.Bot(description="Here is some command for you", command_prefix=commands.when_mentioned_or("p!"), pm_help = False)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+'')
	print('--------')
	print('--------')
	print('Started pubg') #add_your_bot_name_here
	return await client.change_presence(game=discord.Game(name='bc players')) #add_your_bot_status_here


	
client.run(os.getenv('Token'))
