import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix="?")
default_intents = discord.Intents.default()
default_intents.members = True

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command(name='clear')
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()
    for each_message in messages:
        await each_message.delete()

bot.run(os.getenv("TOKEN"))
