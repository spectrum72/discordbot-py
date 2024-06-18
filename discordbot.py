from cmath import log
from distutils.sysconfig import PREFIX
import discord
from discord.ext import commands
from dotenv import load_dotenv
from PyKakao import KoGPT
import os
import asyncio

load_dotenv()
api = KoGPT(service_key = '8597e85508f4673ad4b63a8fa540a834')

#REFIX = os.environ['PREFIX']
CLIENT_TOKEN = os.environ['CLIENT_TOKEN']
COMMAND_PREFIX = "/"

client = commands.Bot(command_prefix=COMMAND_PREFIX, intents=discord.Intents.all())

player = None


@client.event
async def on_ready():
    
    print(f'Logged in as {client.user}.')
    
async def load():
    for file in os.listdir("./Cogs"):
        if file.endswith(".py"):
            await client.load_extension(f".Cogs/{file[:-3]}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == "으응이 손":
        await message.channel.send("손!")
        
    #if message.content == f'{PREFIX}call':
    #    await message.channel.send("callback!")

    #if message.content.startswith(f'{PREFIX}hello'):
    #    await message.channel.send('Hello!')


try:
    client.run(CLIENT_TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")