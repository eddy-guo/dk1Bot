import os, discord, random, pdb # pdb.set_trace()
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

async def duoking1(ctx):
    intlist = [
        "inori",
        "fatorix",
        "krypt",
        "rezz", # "rep would be ruined if picture seen irl"
        "inspiration",
        "triple healing",
        "victim complex",
        "absolute focus",
        "gathering storm",
        "s7",
        "james stephenson",
    ]
    response = "<@" + str(ctx.message.author.id) + "> " + random.choice(intlist)
    await ctx.send("***" + response + "***")