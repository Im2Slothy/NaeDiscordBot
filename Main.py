#Discord Bot Made for Twitch.tv/Naenaehomie discord streaming server! Made By Slothy#4484 ( Any questions Please contact ) https://discord.gg/p8GrXvwxck #


import datetime
import os
import json
import math
import random
from tkinter import Entry
from typing_extensions import Self
import asyncio
import discord
import typing
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)

client = commands.Bot(command_prefix = '.', intents = intents)



#----------MEMBER JOIN AND LEAVE---------- BOT GOING ONLINE -----------------------------

@client.event

async def on_ready():

    print('NaeBot is ready for service!')


@client.event
async def on_member_join(member):
    guild = client.get_guild(665944107025301504)
    channel = guild.get_channel(744834622373756950)
    embed=discord.Embed(title="Welcome!", description=f"Hello, {member.mention} Please read below as there might be some info that is of interest to you!")
    embed.set_author(name="Naenaehomie's Streaming Server", icon_url="https://media.discordapp.net/attachments/618984746977853460/944471778103787570/Logo.png?width=1015&height=571")
    embed.add_field(name="Welcome!", value="Hello and welcome to the official discord streaming server for Naenaehomie! Coming from myself I hope you enjoy, Invite your friends!", inline=True)
    embed.add_field(name="Getting Started", value=f"Before you begin your journey in the server make sure to read the rules and agree to them! If you dare break the rules the mods will come after you!", inline=True)
    embed.add_field(name="Information", value="Once you are an official member of the community we ask that you check the information tap at the top of the discord! You should find things there for any question that you might have!", inline=True)
    embed.add_field(name="Perks", value="Some things that you get while being a part of the community is the chance to meet and game with me! If you are really enjoying the community and want to subcribe you get access to the twitch emote when your discord is linked to your twitch! FYI... You can use this emote anywhere, you dont even need Discord Nitro!", inline=True)
    embed.set_footer(text="Stay cool!")
    role = discord.utils.get(guild.roles, name="Nae's Babies", id=686103426052259855)
    await member.add_roles(role)
    await channel.send(embed=embed)




@client.event

async def on_member_remove(member):

        print(f'{member} has left or was removed from {member.guild}')
#------------------------------------LOGs---------------------------------------------
@client.event
async def on_message_delete(message):
    embed=discord.Embed(title=f"{message.author.name} has deleted a message\nMessage deleted in {message.channel}", color=0xffff)
    embed.add_field(name= message.content ,value="This is the message that has been deleted", inline=True)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f"ID: {message.author.id} ")
    channel=client.get_channel(850007615664553998)
    await channel.send(embed=embed)


@client.event
async def on_message_edit(message_before, message_after):
    embed=discord.Embed(title=f"{message_before.author.name} edited a message\nMessage edited {message_before.channel}!", color=0xffff)
    embed.add_field(name= "Before" ,value= message_before.content, inline=False)
    embed.add_field(name= "After" ,value= message_after.content, inline=False)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f"ID: {message_before.author.id}")
    channel=client.get_channel(850007615664553998)
    await channel.send(embed=embed)





#-----------------------------------------------------------------------------------------

#------------------------------------Commands---------------------------------------------

@client.command(help = "Tells you how many bitches you get... - Made for John")
async def bitches(ctx):
    boi = ["0", "2", "3", "4", "5", "6", "7", "8", "9", "Too many for you to count!"]
    oi = ((random.choice(boi)))
    await ctx.send(f"You pull {oi} bitches!")

@client.command()
async def erepeat(ctx, *, message):
    await ctx.send(message)
    await ctx.message.delete()

@client.command()
async def embed(ctx):
    questions = ["Title?", "Description?"]
    responses = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for question in questions:
        try:
            await ctx.send(question)
            message = await client.wait_for('message', timeout=15, check=check)

        except asyncio.TimeoutError:
            await ctx.send("Timeout")
            return

        else:
            responses.append(message.content)

    embedVar = discord.Embed(title=responses[0], description=responses[1])
    await ctx.send(embed=embedVar)

@client.command()
async def pug(ctx):
    await ctx.send('Bella Puggis Uggis Wuggis!')


@client.command()
async def ping(ctx):
    b=discord.Embed(title=f"Ping?!",description=f"Pong! {round(client.latency * 1000)}ms",color=0xFF5733)
    await ctx.send(embed=b)


@client.command(aliases=['8ball', 'test'])

async def _8ball(ctx,*, question):

    responses = ['It is certain',

                     'It is decidedly so',

                     'Without a doubt',

                     'Yes, definitely',

                     'You may rely on it',

                     'As I see it, yes',

                     'Most likely',

                     'Outlook good',

                     'Yes',

                     'Signs point to yes',

                     'Reply hazy try again',

                     'Ask again later',

                     'Better not tell you now',

                     'Cannot predict now',

                     'Concentrate and ask again',

                     'Do not count on it',

                     'My reply is no',

                     'My sources say no',

                     'Outlook not so good',

                     'Very doubtful']

    b=discord.Embed(title=f"The 8Ball Says!",description=f'Question: {question}\nAnswer: {random.choice(responses)}',color=0x660066)
    await ctx.send(embed=b)  


@client.command()

async def twitch(ctx):
        b=discord.Embed(title=f"The Twitch!",description="https://Twitch.tv/naenaehomie",color=0x6495ED)
        await ctx.send(embed=b)

@client.command()

async def support(ctx):

        b=discord.Embed(title=f"You need help?!",description="If you need help make a ticket inside of #🚸tech-support-form",color=0x6495ED)
        await ctx.send(embed=b)

@client.command(aliases=["mc"])

async def members(ctx):

    a=ctx.guild.member_count
    b=discord.Embed(title=f"Members in {ctx.guild.name}",description=a,color=discord.Color((0xffff00)))
    await ctx.send(embed=b)

#MATH TEST #

def add(n: float, n2: float):
    return n + n2

def sub(n: float, n2: float):
    return n - n2

def rando(n: int, n2: int):
    return random.randint(n, n2)

def div(n: float, n2: float):
    return n / n2

def sqrt(n: float):
    return math.sqrt(n)

def mult(n: float, n2: float):
    return n * n2

@client.command()
async def mathadd(ctx, x: float, y: float):
    try:
        result = add(x, y)
        await ctx.send(result)

    except:
        pass

@client.command()
async def mathsub(ctx, x: float, y: float):
    try:
        result = sub(x, y)
        await ctx.send(result)

    except:
        pass

@client.command()
async def mathrando(ctx, x: int, y: int):
    try:
        result = rando(x, y)
        await ctx.send(result)

    except:
        pass

@client.command()
async def mathdiv(ctx, x: float, y: float):
    try:
        result = div(x, y)
        await ctx.send(result)

    except:
        pass

@client.command()
async def mathmult(ctx, x: float, y: float):
    try:
        result = mult(x, y)
        await ctx.send(result)

    except:
        pass

@client.command()
async def mathsqrt(ctx, x: float):
    try:
        result = sqrt(x)
        await ctx.send(result)

    except:
        pass
#------------------------------------Moderation-------------------------------------------

@client.command(description="Clears Chat!") # Kicks people

@commands.has_role('Server Staff')

async def clear(ctx, amount=5):

        await ctx.channel.purge(limit=amount)

        await ctx.send('messages have been cleared! My work here is done **Dashes away**')



@client.command(description="Kicks People!") # Kicks people

@commands.has_role('Server Staff')

async def kick(ctx, member : discord.Member, *, reason=None):

        await member.kick(reason=reason)
        await ctx.sent(f'{member.mention} has been kicked!')




@client.command(description="Bans People!") # Bans people

@commands.has_role('Server Staff')

async def ban(ctx, user: typing.Union[discord.Member, int], *, reason=None):
    guild = client.get_guild(665944107025301504)
    if user in ctx.guild.members:
        await user.ban(reason=reason)
        await ctx.send(f'Banned {user.mention} My work here is done **Dashes Away**')
        #send banned user a message
        await user.send(f'You have been banned from {guild.name} for {reason}\nFile a ban appeal here: **LINK**')
    else:
        await guild.ban(discord.Object(id = user))
        await ctx.reply(f'User has been hackbanned!\nUser: <@{user}>\nMy work here is done **Bombaclat!**')


@client.command(description="Unbans people!")

@commands.has_role('Server Staff')

async def unban(ctx, *, member):

    obj = await commands.UserConverter().convert(ctx, member)

    if obj is None:

        id_ = await commands.IDConverter().convert(str(member))

        if id_ is not None:

            try:

                obj = await client.fetch_user(int(id_.group(1)))

            except discord.NotFound:

                obj = None

        if obj is None:

            await ctx.send('User not found')

            return 

    await ctx.guild.unban(obj)

    await ctx.send(f'Unbanned {obj} My work here is done **Dashes away**')


@client.command(description="Mutes the specified user.") # Mutes user non timed
@commands.has_role('Server Staff')
async def mute(ctx, member: discord.Member, time, reason=None):
    desctime = time
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    time_convert = {"s":1, "m":60, "h":3600, "d":86400}
    tempmute= int(time[:-1]) * time_convert[time[-1]]
    if not mutedRole:
        mutedRole = discord.utils.get(guild.roles, name="Muted", id=834882506532585533)
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted   for {desctime} ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=True)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await asyncio.sleep(tempmute)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")
    await member.remove_roles(mutedRole)




#-------------------------------------------------------------------------------

client.run('TOKEN')
