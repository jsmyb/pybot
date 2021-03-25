import discord
import random
import asyncio
import webserver
from webserver import keep_alive
import os
from discord.ext import commands


  



bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('mamait het'))
    print('bot is ready..')

@bot.event 
async def on_member_join(member):
    print(f'{member} barew')

@bot.event 
async def on_member_remove(member):
    print(f'{member} oxormi negr')

@bot.command()
# @commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def alo(ctx):
    await ctx.send(f'to du pti ases')

@bot.command()
async def pupul(ctx):
    responses = ['0/10 YAXQ GANDON SIKDIR ES SERVERIC https://i.imgur.com/CHwvp4b.png','1/10 karelia asel puc a','2/10 ahavor pupul, lva mek-mek axpor pes','3/10 gesh pupul','4/10 dzverid mej mi katil jaj chka ay boz','8/10 sirun pupul',' 9/10 lavna pupulikd))','10/10 Cnoxnerd karox en hpartanal ays parahex pupulow']
    await ctx.send(f'{random.choice(responses)}')


keep_alive()

bot.run('NjAyNDg1MDMxOTQ4MjU1MjYy.XTRh6Q.5GZei_pB7P6cuzG52FrTkAAw7-4')