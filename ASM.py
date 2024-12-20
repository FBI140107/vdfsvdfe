# 導入Discord.py模組
import discord
# 導入commands指令模組
from discord.ext import commands

# intents是要求機器人的權限
intents = discord.Intents.all()
# command_prefix是前綴符號，可以自由選擇($, #, &...)
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command()
# 輸入!HKD呼叫指令
async def HKD(ctx):
    await ctx.send("**`付款後請截圖`**")
    await ctx.send("https://cdn.discordapp.com/attachments/1318955645101150238/1318957258910072833/IMG_1664.jpg?ex=6764deeb&is=67638d6b&hm=aa0917d0844c794b7bb5c03c00077f27926732f6cfbc23e4254d80a8f06a6677&")

@bot.command()
async def CM34(ctx):
    await ctx.send("**`付款後請截圖`**")
    await ctx.send("https://www.roblox.com/game-pass/145084359/CM-34")

@bot.command()
async def SAV(ctx):
    await ctx.send("**`付款後請截圖`**")
    await ctx.send("https://www.roblox.com/game-pass/676925697/unnamed")

@bot.command(name='ASMhelp')
async def ASMhelp(ctx):
    await ctx.send("# 指令指南")
    await ctx.send("---------------------------")
    await ctx.send("!HKD 港幣付款碼")
    await ctx.send("!CM34 付款連結")
    await ctx.send("!SAV 付款連結")

bot.run("OTQwNTYzNjUzMDQyNzkwNDIw.GbKzWC.SVYb3AeaGce5Jq88-18xoKnjBPygyHpsFfg0GU")
