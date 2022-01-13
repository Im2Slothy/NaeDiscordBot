#Discord Bot Made for Twitch.tv/Naenaehomie discord streaming server! Made By Slothy#4484 ( Any questions Please contact ) https://discord.gg/p8GrXvwxck #

from os import getenv

import random

import discord

from discord.ext import commands


intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)

client = commands.Bot(command_prefix = '.', intents = intents)



#----------MEMBER JOIN AND LEAVE---------- BOT GOING ONLINE -----------------------------

@client.event

async def on_ready():

    print('NaeBot is ready for service!')



@client.event

async def on_member_join(member):

        print(f'{member} has joined {member.guild}')



@client.event

async def on_member_remove(member):

        print(f'{member} has left or was removed from {member.guild}')



#-----------------------------------------------------------------------------------------

#------------------------------------Commands---------------------------------------------

@client.command()

async def ping(ctx):

        await ctx.send(f'Pong! {round(client.latency * 1000)}ms') # Basic making sure it works command ( Ignore )



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

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')  # 8ball thing



@client.command()

async def twitch(ctx):

        await ctx.send('Twitch: https://www.twitch.tv/naenaehomie :Naenaehomie:') #Nae Twitch command

@client.command()

async def support(ctx):

        await ctx.send('If you need help make a ticket inside of #🚸tech-support-form') #Help meh!
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
        




@client.command(description="Bans People!") # Bans people

@commands.has_role('Server Staff')

async def ban(ctx, member : discord.Member, *, reason=None):

        await member.ban(reason=reason)

        await ctx.send(f'Banned {member.mention} My work here is done **Dashes away**')




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



@client.command(description="Mutes the specified user.")
@commands.has_role('Server Staff')
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Muted {member.mention} for reason {reason} ")
    await member.send(f"You were muted in the server {guild.name} for {reason}")

@client.command(description="Unmutes a specified user.")
@commands.has_role('Server Staff')
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in the server {ctx.guild.name}")


client.run(getenv('TOKEN'))
