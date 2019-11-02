import discord, random, json, asyncio, os
from discord.ext import commands, tasks
from discord.utils import get
from time import sleep
from itertools import cycle

with open("D:/GitHub/Project_Bot_2.0/Data/info.json", "r", encoding="utf8") as jfile:
    data = json.load(jfile)
with open("D:/GitHub/Project_Bot_2.0/Data/token.json", "r", encoding="utf8") as jfile:
    token = json.load(jfile)

ver = data["VER"]
prefix = data["PREFIX"]
name = data["NAME"]
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

english_dice = ["one", "two", "three", "four", "five", "six"]
emojiList = [":voteone:628173653544271892", ":votetwo:628173653552398336",
             ":votethree:628173653586214922", ":votefour:628173653267316739", ":votefive:628173653548204032"]

print(F"\n  >> 正在啟動 {name} <<")

@bot.event
async def on_ready():
    print("  >> 已啟動 <<")


@bot.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title=f"你似乎輸入了錯誤的指令，查看可用指令請使用 {prefix}help 指令", colour=discord.Colour.red())
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed=embed)
        sleep(1)
        await ctx.channel.purge(limit=1)


@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title=F"**📚  {name} 指令大全**", description=F"{ver}", colour=discord.Colour.orange())
    embed.add_field(name=F"🌀  {prefix}clear [數量]", value="清除訊息", inline=False)
    embed.add_field(name=F"🎲  {prefix}dice", value="骰子功能，可以投擲骰子 1-6 號", inline=False)
    embed.add_field(name=F"📙  {prefix}help", value="查詢本機器人的功能", inline=False)
    embed.add_field(name=F"🤖  {prefix}openbot", value="查詢本機器人的官方網站", inline=False)
    embed.add_field(name=F"🌐  {prefix}ping", value="查詢你的網路延遲度（稱為 Ping 值）", inline=False)
    embed.add_field(name=F"📣  {prefix}vote [get/remove]", value="使用後，你將獲得或取消 [投票通知] 身分組", inline=False)
    embed.set_thumbnail(url="https://raw.githubusercontent.com/open3/OpenBot/master/Res/report.png")
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)


@bot.command()
async def dice(ctx):
    num = random.randint(1, 6)
    embed = discord.Embed(title=F"{name} 骰子功能", description="**你骰到了 {}**".format(num), color=0xbf0202)
    embed.set_thumbnail(url="https://raw.githubusercontent.com/open3/OpenBot/master/Res/dice{}.png".format(english_dice[num - 1]))
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)


@bot.command()
async def openbot(ctx):
    embed = discord.Embed(title="https://open3.github.io/OpenWeb/", description="連結至 OpenBot 官方網站", colour=discord.Colour.purple())
    embed.set_thumbnail(url="https://raw.githubusercontent.com/open3/OpenBot/master/Res/githublink.png")
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)
    

@bot.command()
async def ping(ctx):
    embed = discord.Embed(colour=discord.Colour.blue())
    embed.set_author(name="你的延遲數為 {} 毫秒 (ms) ".format(round(bot.latency*1000)), icon_url="https://cdn3.iconfinder.com/data/icons/flat-pro-basic-set-3/32/internet-512.png")
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)


@bot.command()
async def vote(ctx, option): 
    role = discord.utils.get(ctx.guild.roles, name="投票通知")
    user = ctx.message.author
    await ctx.channel.purge(limit=1)
    if option == "get":
        embed = discord.Embed(title="**投票通知身分組已給予！**", description="\n你將會在 Discord 群上\n接收到全部的投票" , colour=discord.Colour.green())
        embed.set_thumbnail(url="https://raw.githubusercontent.com/open3/OpenBot/master/Res/vote.png")
        await user.add_roles(role)
    elif option == "remove":
        embed = discord.Embed(title="**投票通知身分組已取消！**", description="\n你將不會在 Discord 群上\n接收到全部的投票" , colour=discord.Colour.red())
        embed.set_thumbnail(url="https://raw.githubusercontent.com/open3/OpenBot/master/Res/noremove.png")
        await user.remove_roles(role)
    await ctx.send(embed=embed)


@bot.command()
async def clear(ctx, amount=0):
    await ctx.channel.purge(limit=amount+1)
    user_name = ctx.author
    user_id = ctx.author.id
    embed = discord.Embed(title=f"你已清除 {amount} 條訊息", colour=discord.Colour.blurple())
    await user_name.send(embed=embed)


bot.run(token["TOKEN"])
