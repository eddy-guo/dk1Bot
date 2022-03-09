import os, discord, random, pdb, asyncio
# create breakpoints for debugging with pdb
    # use pdb.set_trace() to stop at certain line
    # c n s q: https://poweruser.blog/setting-a-breakpoint-in-python-438e23fe6b28
import dk1, cf # file names for function referencing
from dotenv import load_dotenv
from discord.ext import commands

# removes runtime error but makes ctrl-c slow af
# https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# env file with bot token and guild id
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# change intents of bot to include all members; INTENTS REMOVED FROM OTHER FILES, MIGHT CAUSE ISUES
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

# on_ready print info
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

# welcome message
@bot.event
async def on_member_join(member): # once a member joins,
    await member.create_dm() # create a dm with them,
    await member.dm_channel.send( # and send them a message
        f'Hi {member.name}, welcome to ***{guild.name}***.'
    )

# per message, update global dictionary
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

# https://realpython.com/how-to-make-a-discord-bot-python/
    # last part: admin/profile
    # research find(), get(), and lambda

# crypto; nft start again, moralis?



# FOR TTT LEARNING PROCESS https://github.com/afazio1/robotic-nation-proj/blob/master/projects/discord-bot/tictactoe.py

# future

# classes for ttt in order to call functions and play the game on bot.py
    # can also make new instances of classes to play multiple games at once

# when command is ran, send description of how game is played and command rules
    # !dk1, !cf as well

# connect with bot.py; should this be done before or after on_message? (see below)

# figure out how to run ttt in bot, easy way
    # after, consider future

# on_message; make the code cleaner, seperate response messages
    # lots of logic has to be changed...
        # !tictactoe: "Who would you like to play with?"
        # !place doesn't change

# win = print message, nothing else; keep a list of total wins? something meaningful?
    # database with top winners

# buttons on tictactoe...

# long term goal
    # Go + Connect 4(5??) + TTT game...
        # winning conditions completely changed, logic instead of hard code (fk)
        # hard code the 15x15 board?
        # coordinate system instead of 1-9?

# word game?
# league related trivia games?
    # start game; bot joins call, plays a voice line from champ, exits; players guess
    # point system, guessing, locking in answer, etc etc