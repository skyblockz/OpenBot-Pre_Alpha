import discord, json
from discord.ext import commands, tasks
from itertools import cycle


with open("D:/GitHub/Project_Bot_2.0/Data/info.json", "r", encoding="utf8") as jfile:
    data = json.load(jfile)
with open("D:/GitHub/Project_Bot_2.0/Data/token.json", "r", encoding="utf8") as jfile:
    token = json.load(jfile)

bot = commands.Bot(command_prefix=data["PREFIX"])
ver = data["VER"]

@bot.event
async def on_ready():
    print("\n  >> 已啟動 <<")
    status = cycle([F"{ver} Pre-Alpha"])
    await bot.change_presence(activity=discord.Game(next(status)))


@bot.event
async def on_message(message):
    msg = message.content
    try:
        commands(ctx)

@bot.command()
async def commands(ctx):
    return

bot.run(token["TOKEN"])
