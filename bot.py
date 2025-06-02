from config import *

import discord
from discord.ext import commands

prefix = "/"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(commond_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected")

@bot.command(name='greet')
async def greet(ctx):
    await ctx.send("Ribbit!")

@bot.command(name='whoami')
async def whoami(ctx):
    await ctx.send(f"{ctx.author}-frog")

bot.run(bot_token)
