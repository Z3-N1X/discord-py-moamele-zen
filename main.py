import os

from replit import db
import asyncio
import discord
from discord.ext import commands 


inte = discord.Intents.all()
 
bot = commands.Bot(command_prefix=".", intents =inte)

try:
  print(db["servers"])
except:
  db["servers"] = {}
  
@bot.event
async def on_ready():
  print("online!")




async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
      




Token = os.environ['Token']
async def main():
    async with bot:
        
        await load_extensions()
        await bot.start(Token)

asyncio.run(main())

