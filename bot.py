from config import *

import discord
from discord.ext import commands
import datetime
import pytz

prefix = "/"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected!")

@bot.command(name='greet')
async def greet(ctx):
    await ctx.send("Ribbit!")

@bot.command(name='whoami')
async def whoami(ctx):
    await ctx.send(f"{ctx.author}-frog")

@bot.command(name='la_time')
async def la_time(ctx, year, month, day, hour, min):
    try:
        date = datetime.datetime(int(year), int(month), int(day), int(hour), int(min))
        la_tz = pytz.timezone("America/Los_Angeles")
        la_date = la_tz.localize(date)
        await ctx.send(la_date)
    except:
        await ctx.send("Something went wrong")

@bot.command(name='utc_time', description='LA -> UTC')
async def utc_time(ctx, year, month, day, hour, min):
    try:
        date = datetime.datetime(int(year), int(month), int(day), int(hour), int(min))
        la_tz = pytz.timezone("America/Los_Angeles")
        la_date = la_tz.localize(date)
        utc_date = la_date.astimezone(pytz.utc)
        await ctx.send(utc_date)
    except:
        await ctx.send("Something went wrong")

bot.run(bot_token)
