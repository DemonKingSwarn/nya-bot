import sys
import discord
from discord.ext import commands
import aiohttp
import asyncio
import json
import re
import tracemalloc
import os
import requests
tracemalloc.start()

with open('config/config.json') as f:
    config = json.load(f)
    token = config['token']
    prefix = config['prefix']

bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_ready():
    print("logged in!")

@bot.event
async def on_message(message):
    
    if message.author == bot.user:
        return

    if message.content.startswith('nya|ping'):
        await message.channel.send('Pong! {0}'.format(round(bot.latency, 1)))


    if message.author.id == 453522683745927178:
        if message.content.startswith("\>") or message.content.startswith("nya"):
            return
        m = str(message.content)
        await message.delete()
        await message.channel.send(m +' ,nya〜')

bot.run(token)
