import os, discord, pdb
# create breakpoints for debugging with pdb
    # use pdb.set_trace() to stop at certain line
    # c n s q: https://poweruser.blog/setting-a-breakpoint-in-python-438e23fe6b28
import dk1, cf # file names for function referencing
from dotenv import load_dotenv
from discord.ext import commands

# removes runtime error but makes ctrl-c slow af
# https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
# import asyncio, asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    global guild
    guild = discord.utils.get(bot.guilds, name=GUILD)
    global user_messages
    user_messages = {}
    for member in guild.members:
        user_messages[member.name] = "filler"

    if guild is None:
        print("Bot is not registered under that guild.") # .env is wrong, guild user does not exist (name!=GUILD)
        return

    members = '\n - '.join([member.name for member in guild.members])
    print(
        f'\n{bot.user} is connected to the following guild:\n'
        f'{guild.name} (id: {guild.id})\n\n'
        f'Guild Members:\n - {members}'
    )

@bot.event
async def on_member_join(member): # once a member joins,
    await member.create_dm() # create a dm with them,
    await member.dm_channel.send( # and send them a message
        f'Hi {member.name}, welcome to ***{guild.name}***.'
    )

@bot.event
async def on_message(message): # once a message is sent
    if message.author == bot.user: # do not make bot respond to bot
        return
    ctx = await bot.get_context(message) # passing ctx into an on_message function
    if message.content == "!cf":
        response = "***Flip it, " + "<@" + str(message.author.id) + '>! Please input "heads" or "tails".***'
        await ctx.send(response)
    elif message.content == "!dk1":
        await dk1.duoking1(ctx)

    for user in user_messages:
        if user_messages[user] == "!cf" and user == message.author.name: # think
            await cf.coinflip(ctx, message.content)
    user_messages[message.author.name] = message.content # update global dictionary and print
    print(user_messages)

bot.run(TOKEN)