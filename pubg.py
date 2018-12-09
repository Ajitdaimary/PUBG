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
import json
import textwrap
#from .cogs.utils.utils import Utils
from .AudioNode import AudioNode
from .AudioPlayer import AudioPlayer
from .Events import TrackStart
import websockets
from pyee import EventEmitter
from .Events import TrackEnd
#from utils.Logger import Logge
from .Events import TrackStart, QueueConcluded
from .AudioTrack import AudioTrack
from discord import User



client = commands.Bot(description="Here is some command for you", command_prefix=commands.when_mentioned_or("p!"), pm_help = False)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+'')
	print('--------')
	print('--------')
	print('Started Soyal') #add_your_bot_name_here
	return await client.change_presence(game=discord.Game(name='PUBG')) #add_your_bot_status_here

@client.event
async def on_message(message):
    channel = client.get_channel('519791076803084288')
    if message.server is None and message.author != client.user:
        await client.send_message(channel, '{} : <@{}> : '.format(message.author.name, message.author.id) + message.content)
    await client.process_commands(message)

@client.command(pass_context=True)
async def ownerinfo(ctx):
    embed = discord.Embed(title="Information about owner", description="Bot Name- MARCOS", color=0x00ff00)
    embed.set_footer(text="MARCOS")
    embed.set_author(name=" Bot Owner Name- MARCOS,498378677512437762")
    embed.add_field(name="Site- coming soon...", value="Thanks for adding our bot", inline=True)
    await client.say(embed=embed)
	
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
@commands.cooldown(rate=5,per=86400,type=BucketType.user) 
async def access(ctx, member: discord.Member):
    if ctx.message.author.bot:
      return
    else:
      role = discord.utils.get(member.server.roles, name='access')
      await client.add_roles(member, role)
      await client.say("Gave access to {}".format(member))
      for channel in member.server.channels:
        if channel.name == 'soyal-log':
            embed=discord.Embed(title="User Got Access!", description="**{0}** got access from **{1}**!".format(member, ctx.message.author), color=0x020202)
            await client.send_message(channel, embed=embed)
            await asyncio.sleep(45*60)
            await client.remove_roles(member, role)
		
@client.event
async def on_member_join(member):
    print("In our server" + member.name + " just joined")
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Welcome message')
    embed.add_field(name = '__Welcome to Our Server__',value ='**Thanks for Joining our Server Hope you enjoy please respect all members and staff.**',inline = False)
    embed.set_image(url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')
    await client.send_message(member,embed=embed)
    print("Sent message to " + member.name)
    channel = discord.utils.get(client.get_all_channels(), server__name='bysoyal2', name='welcome')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check Rules and never try to break any one of them', color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name='__Thanks for joining__', value='**Hope you will be active here.**', inline=True)
    embed.add_field(name='Your join position is', value=member.joined_at)
    embed.set_image(url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')
    embed.set_thumbnail(url=member.avatar_url)
    await client.send_message(channel, embed=embed)

@client.command(pass_context=True)
async def poll(ctx, question, *options: str):
        if len(options) <= 1:
            await client.say('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await client.say('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['👍', '👎']
        else:
            reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=question, description=''.join(description), color = discord.Color((r << 16) + (g << 8) + b))
        react_message = await client.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await client.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await client.edit_message(react_message, embed=embed)

@client.command(pass_context = True)
async def avatar(ctx, user: discord.Member=None):
    if user is None:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar', description='Avatar is profile picture of a user in discord', color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name='User: {}'.format(ctx.message.author.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/520159870448566287/520829749095038977/pubg.png') 
        embed.set_image(url = ctx.message.author.avatar_url)
        await client.say(embed=embed)
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar', description='Avatar is profile picture of a user in discord', color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name='User: {}'.format(user.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/520159870448566287/520829749095038977/pubg.png') 
        embed.set_image(url = user.avatar_url)
        await client.say(embed=embed)

	
@client.command(pass_context = True)
async def meme(ctx):
    choices = ['https://img.memecdn.com/english_o_869587.webp', 'https://img.memecdn.com/everybody-knows-muricans-don-amp-039-t-speak-english-the-same-way-mexicans-don-amp-039-t-speak-spanish_c_7233205.webp', 'https://img.memecdn.com/english-reaction-when-they-heard-about-eu_c_6994013.webp', 'https://images3.memedroid.com/images/UPLOADED393/5b0c3ee92799f.jpeg' , 'https://images7.memedroid.com/images/UPLOADED850/5b0c2d7dd6049.jpeg', 'https://images7.memedroid.com/images/UPLOADED905/5b0c30c468fa8.jpeg', 'https://images7.memedroid.com/images/UPLOADED726/5b0c2d4c5f288.jpeg', 'https://images7.memedroid.com/images/UPLOADED936/5b0c2a90adbe7.jpeg', 'https://images7.memedroid.com/images/UPLOADED764/5b0c1e491c669.jpeg', 'https://images3.memedroid.com/images/UPLOADED922/5b0c284b71cd0.jpeg', 'https://images3.memedroid.com/images/UPLOADED207/5b0c265a58cf4.jpeg', 'https://images7.memedroid.com/images/UPLOADED920/5b0c06813741a.jpeg', 'https://images3.memedroid.com/images/UPLOADED46/5a91c871e61f1.jpeg', 'https://images7.memedroid.com/images/UPLOADED737/5a91c7f234bd2.jpeg', 'https://images7.memedroid.com/images/UPLOADED757/5a91bd39e1323.jpeg', 'https://images7.memedroid.com/images/UPLOADED963/5a91b4f7aba7e.jpeg', 'https://images7.memedroid.com/images/UPLOADED794/5a91ac0900506.jpeg', 'https://images3.memedroid.com/images/UPLOADED188/5a91aa326ad4e.jpeg']
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title='Meme', description='<a:OnThaCoco:515853700682743809><a:OnThaCoco:515853700682743809><a:OnThaCoco:515853700682743809>', color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/520159870448566287/520829749095038977/pubg.png') 
    embed.set_image(url = random.choice(choices))
    await client.send_typing(ctx.message.channel)
    await client.send_message(ctx.message.channel, embed=embed) 

	
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def dm(ctx, user: discord.Member, *, msg: str):
    try:
        await client.send_message(user, msg)
        await client.delete_message(ctx.message)          
        await client.say("Success! Your DM has made it! :white_check_mark: ")
    except discord.ext.commands.MissingPermissions:
        await client.say("Aw, come on! You thought you could get away with DM'ing people without permissions.")
    except:
        await client.say("Error :x:. Make sure your message is shaped in this way: p!dm [tag person] [msg]")
	
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
async def unmute(ctx, member: discord.Member=None):
    if member is None:
      await client.say('Please specify member i.e. Mention a member to unmute. Example- ``mv!unmute @user``')
    if ctx.message.author.bot:
      return
    else:
      role = discord.utils.get(member.server.roles, name='Muted')
      await client.remove_roles(member, role)
      await client.say("Unmuted **{}**".format(member))
      for channel in member.server.channels:
        if channel.name == '???-multiverse-log-???':
            embed=discord.Embed(title="User unmuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xFD1600)
            await client.send_message(channel, embed=embed)
		
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User=None, *, message:str=None): 
    if userName is None:
      await client.say('Please tag a person to warn user. Example- ``mv!warn @user <reason>``')
      return
    else:
      await client.send_message(userName, "You have been warned for: **{}**".format(message))
      await client.say(":warning: __**{0} Has Been Warned!**__ :warning: ** Reason:{1}** ".format(userName,message))
      pass

@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def kick(ctx,user:discord.Member):
    if user is None:
      await client.say('Please mention a member to kick. Example- ``mv!kick @user``')
    if user.server_permissions.kick_members:
      await client.say('**He is mod/admin and i am unable to kick him/her**')
      return
    else:
      await client.kick(user)
      await client.say(user.name+' was kicked. Good bye '+user.name+'!')
      await client.delete_message(ctx.message)
      for channel in user.server.channels:
        if channel.name == '???-multiverse-log-???':
            embed=discord.Embed(title="User kicked!", description="**{0}** is kicked by **{1}**!".format(user, ctx.message.author), color=0xFDE112)
            await client.send_message(channel, embed=embed)
		
@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def bans(ctx):
    '''Gets A List Of Users Who Are No Longer With us'''
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of The Banned Idiots", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)

@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     
async def unban(ctx):
    ban_list = await client.get_bans(ctx.message.server)

    # Show banned users
    await client.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

    # Unban last banned user
    if not ban_list:
      await client.say('Ban list is empty.')
      return
    else:
      await client.unban(ctx.message.server, ban_list[-1])
      await client.say('Unbanned user: `{}`'.format(ban_list[-1].name))
      for channel in member.server.channels:
        if channel.name == '???-multiverse-log-???':
            embed=discord.Embed(title="User unbanned!", description="**{0}** unbanned by **{1}**!".format(ban_list[-1].name, ctx.message.author), color=0x38761D)
            await client.send_message(channel, embed=embed)
		
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)     
async def userinfo(ctx, user: discord.Member=None):
    if user is None:
        await client.say('Please tag a user to get user information. Example- ``mv!userinfo @user``')
    if ctx.message.author.bot:
      return
    else:
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
      embed.add_field(name="Name", value=user.name, inline=True)
      embed.add_field(name="ID", value=user.id, inline=True)
      embed.add_field(name="Status", value=user.status, inline=True)
      embed.add_field(name="Highest role", value=user.top_role)
      embed.add_field(name="Joined", value=user.joined_at)
      embed.set_thumbnail(url=user.avatar_url)
      await client.say(embed=embed)

@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     

async def serverinfo(ctx):
    '''Displays Info About The Server!'''

    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))

    roles = ', '.join(roles);
    channelz = len(server.channels);
    time = str(server.created_at); time = time.split(' '); time= time[0];
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', color = discord.Color((r << 16) + (g << 8) + b));
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = '__ID__', value = str(server.id))
    join.add_field(name = '__Member Count__', value = str(server.member_count));
    join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='Created: %s'%time);

    return await client.say(embed = join);

@client.command(pass_context=True, aliases=['server'])
@commands.has_permissions(kick_members=True)
async def membercount(ctx, *args):
    """
    Shows stats and information about current guild.
    ATTENTION: Please only use this on your own guilds or with explicit
    permissions of the guilds administrators!
    """
    if ctx.message.channel.is_private:
        await bot.delete_message(ctx.message)
        return

    g = ctx.message.server

    gid = g.id
    membs = str(len(g.members))
    membs_on = str(len([m for m in g.members if not m.status == Status.offline]))
    users = str(len([m for m in g.members if not m.bot]))
    users_on = str(len([m for m in g.members if not m.bot and not m.status == Status.offline]))
    bots = str(len([m for m in g.members if m.bot]))
    bots_on = str(len([m for m in g.members if m.bot and not m.status == Status.offline]))
    created = str(g.created_at)
    
    em = Embed(title="Membercount")
    em.description =    "```\n" \
                        "Members:   %s (%s)\n" \
                        "  Users:   %s (%s)\n" \
                        "  Bots:    %s (%s)\n" \
                        "Created:   %s\n" \
                        "```" % (membs, membs_on, users, users_on, bots, bots_on, created)

    await client.send_message(ctx.message.channel, embed=em)
    await client.delete_message(ctx.message)
	
class AudioManager:
    """
    Class of the AudioManager section.
    This is main class and controls all stuff like joining channels, leaving channels, and launching nodes.
    """
    def __init__(self, bot, nodes, shards=1):
        self.bot = bot
        bot.add_listener(self.on_socket_response)
        self.nodes = {}
        self.players = {}
        self._nodes = nodes
        self.shards = shards
        self.session = self.bot.session
        self.utils = self.bot.utils

    def get_player(self, ctx):
        player = self.players.get(ctx.guild.id)
        if player is None:
            player = AudioPlayer(ctx, self, self.nodes.get(self._nodes[0]["host"]))
            self.players[ctx.guild.id] = player

        return player

    async def get_tracks(self, player, search: str):
        async with self.session.get(f"http://{player.node.host}:2333/loadtracks?identifier={search}", headers={"Authorization": player.node.password}) as resp:
            tracks = await resp.json()
            return tracks
    
    async def on_socket_response(self, data):
        if data["t"] == "VOICE_SERVER_UPDATE":
            payload = {
                "op": "voiceUpdate",
                "guildId": data["d"]["guild_id"],
                "sessionId": self.bot.get_guild(int(data["d"]["guild_id"])).me.voice.session_id,
                "event": data["d"]
            }
            await self.nodes.get(self._nodes[0]["host"]).send(**payload)

    async def connect(self, ctx):
        await self.bot.ws.send(json.dumps({
            "op": 4,
            "d": {
                "guild_id": ctx.guild.id,
                "channel_id": ctx.author.voice.channel.id,
                "self_mute": False,
                "self_deaf": False
            }
        }))
        self.get_player(ctx).is_connected = True

    async def leave(self, ctx):
        await self.bot.ws.send(json.dumps({
            "op": 4,
            "d": {
                "guild_id": ctx.guild.id,
                "channel_id":  None,
                "self_mute": False,
                "self_deaf": False
            }
        }))
        try:
            del self.players[ctx.guild.id]
        except KeyError:
            pass
        
    async def audio_task(self):
        for i in range(len(self._nodes)):
            node = AudioNode(self, self.shards, self._nodes[i]["host"], self._nodes[i]["password"], self._nodes[i]["port"])
            await node.launch()
            self.nodes[node.host] = node
        self.bot.loop.create_task(self.node_event_task())

    async def node_event_task(self):

        for node in self.nodes.values():
            @node.ee.on("track_start")
            async def on_track_start(e):
                print("Music: track_start event triggered.")
                ctx = e.player.ctx
                #print(dir(e))
                f = e
                e = e.track
                #print(dir(e))
                em = discord.Embed(color=0x00ff00, title=f"Music")
                #em.description = f"**{e.track.title}**"
                em.set_author(name=e.requester.name, icon_url=e.requester.avatar_url)
                second = e.length / 1000
                minute, second = divmod(second, 60)
                hour, minute = divmod(minute, 60)
                #minutes, seconds = divmod(e.track.duration, 60)
                #em.add_field(name='Length', value=f"{str(minutes)}:{str(seconds).replace('0', '00').replace('1', '01').replace('2', '02').replace('3', '03').replace('4', '04').replace('5', '05').replace('6', '06').replace('7', '07').replace('8', '08').replace('9', '09')}")
                if hour:
                    length = f"{int(hour)}:{self.utils.format_time(minute)}:{self.utils.format_time(second)}"
                else:
                    length = f"{self.utils.format_time(minute)}:{self.utils.format_time(second)}"
                playing_panel = textwrap.dedent(f"""
I started playing the music! {self.bot.get_emoji(511089456196091916)}
:musical_note: **Song**
{e.title}
{self.bot.get_emoji(430340802879946773)} **Requested By**
{str(ctx.author)}
:timer: **Length**
{length}
:loud_sound: **Volume**
{f.player.volume}
:1234: **Queue Position**
{len(f.player.queue)}
                """)
                #em.add_field(name='Length', value=length)
                #em.add_field(name='Volume', value=f"{self.utils.get_lines(e.player.volume)} {e.player.volume}%")
                em.description = playing_panel
                #em.add_field(name='Position in Queue', value=len(e.player.queue))
                msg = await ctx.send(embed=em, edit=False)
                try:
                    await msg.add_reaction("\U000023f8") # Pause
                    await msg.add_reaction("\U000025b6") # Play/Resume
                    await msg.add_reaction("\U000023f9") # Stop
                    await msg.add_reaction("\U0001f501") # Repeat
                    await msg.add_reaction("\U00002753") # Help
                except discord.Forbidden:
                    return await ctx.send("I don't have Add Reaction permissions, so I can't show my awesome playing panel!")
                try:    
                    while f.player.playing:
                        if len(ctx.author.voice.channel.members) <= 1:
                            return await ctx.send(f"Guys? Seriously? Well, guess I'm out too. {self.bot.get_emoji(517142988904726562)}")
                        reaction, user = await self.bot.wait_for("reaction_add", check=lambda r, u: u.id == ctx.author.id and r.emoji in "⏸▶⏹🔁❓")
                        if reaction.emoji == "⏸":
                            await e.pause()
                            try:
                                await msg.remove_reaction("\U000023f8", user)
                            except: 
                                pass
                        elif reaction.emoji == "▶":
                            await e.resume()
                            await msg.remove_reaction("\U000025b6", user)
                        elif reaction.emoji == "⏹":
                            e.player.queue.clear()
                            await e.stop()
                            await msg.delete()
                        elif reaction.emoji == "🔁":
                            e.repeating = not e.repeating
                            await msg.remove_reaction("\U0001f501", user)
                        elif reaction.emoji == "❓":
                            await msg.remove_reaction("\U00002753", user)
                            embed = discord.Embed(color=0x00ff00, title='Music Player Help')
                            embed.description = "**What do these magical buttons do?** \n\n:pause_button: Pauses the current song.\n:arrow_forward: Resumes any currently paused song.\n:stop_button: Stops the playing song and deletes this message.\n:repeat: Starts the current song from the beginning.\n:question: Shows this message."
                            embed.set_footer(text='This will revert back in 15 seconds.')
                            await msg.edit(embed=embed)
                            await asyncio.sleep(15)
                            await msg.edit(embed=em)
                except discord.Forbidden:
                    pass # No need to send 
                # except Exception as e:
                #     return await ctx.send(f"An unknown error occured. Details: \n\n```{e}```")

                # This made shit way too spammy, can't think of a good way to avoid it, rather just remove it.

            @node.ee.on("track_end")
            async def on_track_end(event):
                print("Music: track_end event triggered.")
                if event.reason == "REPLACED":
                    return  # Return because if we play then the queue will be fucked.
                elif event.reason == "FINISHED":
                    if event.player.repeating:
                        await event.player.node.send(op="play", guildId=str(event.player.ctx.guild.id), track=event.player.current.track)
                        return event.player.node.ee.emit("track_start", TrackStart(event.player, event.player.current))
                    await event.player.play()

            @node.ee.on("queue_concluded")
            async def on_queue_concluded(event):
                print("Music: queue_concluded event triggered.")
                await self.leave(event.player.ctx)
		
class AudioNode:
    def __init__(self, manager, shards, host=None, password=None, port=None):
        self.stats = {}
        self.ee = EventEmitter()
        self._manager = manager
        self.shards = shards
        self.ready = False
        self.ws = None
        self.host = host
        self.password = password
        self.port = port
        self.stats = None
        self.reconnect_tries = 0

    def __str__(self):
        return f"""
A lavalink node class for the lavalink manager.
Shards: {self.shards}
Host: {self.host}
Port: {self.port}"""

    async def _wait_for_ws_message(self):
        while self.ws.open:
            try:
                data = json.loads(await self.ws.recv())
            except websockets.ConnectionClosed:
                return self._manager.bot.loop.create_task(self.launch())

            if data["op"] == "playerUpdate":
                player = self._manager.players.get(int(data["guildId"]))
                if player:
                    player.state["timestamp"] = data["state"]["time"]
                    player.state["position"] = data["state"]["position"]
            elif data["op"] == "stats":
                del data["op"]
                self.stats = data
            elif data["op"] == "event":
                player = self._manager.players.get(int(data["guildId"]))
                if data["type"] == "TrackEndEvent":
                    if player:
                        self.ee.emit("track_end", TrackEnd(player, data["track"], data["reason"]))

    def _headers(self):
        return {
            "Authorization": self.password,
            "Num-Shards": self.shards,
            "User-Id": self._manager.bot.user.id
        }

    async def launch(self):
        try:
            self.ws = await websockets.connect(f"ws://{self.host}:{self.port}", extra_headers=self._headers())
            if self.ws.open:
                self._manager.bot.loop.create_task(self._wait_for_ws_message())
                self.ready = True
        except OSError as error:
            pass

    async def send(self, **data):
        if self.ws.open:
            await self.ws.send(json.dumps(data))
	
	
class AudioPlayer:
    """
    Class of AudioPlayer.
    This class has many uses.
    It can play music, skip music, pause music, resume music, seek music, and much more.
    """
    def __init__(self, ctx, manager, node):
        self.ctx = ctx
        self.state = {}
        self.manager = manager
        self.node = node
        self.volume = 50
        self.playing = False
        self.paused = False
        self.repeating = False
        self.current = None
        self.is_connected = False
        self.queue = []
        self.m = None

    def enqueue(self, track: dict, requester: User):
        self.queue.append(AudioTrack().make(track, requester))

    async def play(self):
        if not self.queue:
            self.node.ee.emit("queue_concluded", QueueConcluded(self.manager.get_player(self.ctx)))
        else:
            self.playing = True
            track = self.queue.pop(0)
            self.current = track
            await self.node.send(op="play", guildId=str(self.ctx.guild.id), track=track.track)
            self.node.ee.emit("track_start", TrackStart(self.manager.get_player(self.ctx), track))

    async def stop(self):
        await self.node.send(op="stop", guildId=str(self.ctx.guild.id))

    async def set_paused(self, paused):
        self.paused = paused
        await self.node.send(op="pause", guildId=str(self.ctx.guild.id), pause=self.paused)

    @staticmethod
    def valid_volume(volume):
        return 10 <= volume <= 150

    async def set_volume(self, volume):
        if not self.valid_volume(volume):
            return
        self.volume = volume
        await self.node.send(op="volume", guildId=str(self.ctx.guild.id), volume=volume)
	
class AudioTrack:
    def make(self, track, requester):
        try:
            self.track = track["track"]
            self.id = track["info"]["identifier"]
            self.seekable = track["info"]["isSeekable"]
            self.author = track["info"]["author"]
            self.length = track["info"]["length"]
            self.stream = track["info"]["isStream"]
            self.title = track["info"]["title"]
            self.url = track["info"]["uri"]
            self.requester = requester

            return self
        except KeyError:
            raise Exception("Invalid track passed: {}".format(str(track)))

	
class TrackStart:
    def __init__(self, player, track):
        self.player = player
        self.track = track


class TrackEnd:
    def __init__(self, player, track, reason):
        self.player = player
        self.track = track
        self.reason = reason


class QueueConcluded:
    def __init__(self, player):
        self.player = player	
	
client.run(os.getenv('Token'))
