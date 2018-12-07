import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!!' )
Clientdiscord = discord.Client()


@client.event
async def on_ready():
	await client.change_presence(game=Game(name='Killing'))
	print('Ready, Freddy')

@client.event
async def on message(message):
	if message.content == '!!hi':
		await client.sand_message(message.channel, 'Hello')
		
client.run('TOKEN')
