from config import *

import discord
from discord.ext import commands
from datetime import datetime
import pytz

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

'''@bot.command(name='gettime', hour, min, month, day, year)
async def gettime(ctx, hour, minute, month, day, year):
    la_time = pytz.timezone("America/Los_Angeles")
    hour = hour
    min = min
    month = month
    day = day
    year = year

    try:
        date = datetime(year, month, day, hour, min)
        la_date = la_time.localize(date)
        ctx.send(la_date)
    except:
        ctx.send("Something went wrong")
'''
bot.run(bot_token)
