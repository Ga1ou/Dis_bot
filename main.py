import discord
from discord.ext import commands 
import json

with open('setting.json','r', encoding='utf-8') as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix= '[')





@bot.event

async def on_ready():
    print(">> Bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(572283016853061634)
    await channel.send(f'{member}just joined, We1come!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(572283016853061634)
    await channel.send(f'{member}leave!')

@bot.command()
async def ping(ctx):
    await ctx.send('Greedings, nerds and virgins')

@bot.command()
async def image(ctx):
    pic = discord.File(jdata['pic'])
    await ctx.send(file = pic)

bot.run(jdata['TOKEN'])