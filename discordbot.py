import discord
from discord.ext import commands
from myCrypto import coin_tweet
import time
from chatgpt import test
import gpt4all
import os

KEY = os.environ['DISCORDKEY']
TOKEN = os.environ['DISCORDTOKEN']
prefix = '!'
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=prefix, intents=intents)
quit = False



@bot.event
async def on_ready():
    print("bot is ready")

@bot.command()
async def hello(ctx):
    await ctx.send("nice to meet you")

@bot.command()
async def myCoins(ctx):
    count = 0
    user_id = ctx.author.id
    while count!=6:
        coin_list = [coin_tweet("ethereum", "ETH"), coin_tweet("internet-computer", "ICP"), coin_tweet("chainlink","LINK"), coin_tweet("bitcoin", "BTC")]
        for coin in coin_list:
            await ctx.send(f'{coin}')
        await ctx.send(f'<@{user_id}>')
        count+=1
        time.sleep(1800)

@bot.command()
async def quit(ctx):
    print("quitting")
    global quit
    await ctx.send('quitting')  
    quit = True

@bot.command()
async def coininfo(ctx, name, symbol):
    user_id = ctx.author.id
    symbol = symbol.upper()
    name = name.lower()
    await ctx.send(coin_tweet(name, symbol)+ f' <@{user_id}>')

@bot.command()
async def chat(ctx,*, prompt):
    
    await ctx.send("working...")
    await ctx.send(test(prompt))
    await ctx.send("done!")
    print(test(prompt))


bot.run(TOKEN)
