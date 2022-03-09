import os, discord, random, pdb
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command()
async def coinflip(ctx, input):
    options = ["heads", "tails"]
    correct = random.choice(options)
    if input not in options:
        response = "***<@" + str(ctx.message.author.id) + '>, that is not a side of a coin. Please run the command again and input "heads" or "tails" afterward.***'
        await ctx.send(response)
        return
    if input == correct:
        response = "***The coin landed on " + correct + ". Congratulations" + "<@" + str(ctx.message.author.id) + ">, you win!***"
        await ctx.send(response)
    else:
        response = "***The coin landed on " + correct + ". Better luck next time, " + "<@" + str(ctx.message.author.id) + ">.***"
        await ctx.send(response)
