import discord

from discord import app_commands
from discord.ext import commands

from dotenv import load_dotenv # library to put tokens, passwords, api keys etc.
import os # to get token
import asyncio

load_dotenv() # Get token from .env
token = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.all()     # Specify all bots intents(all because idk what i actually have to give him)
bot = commands.Bot(command_prefix = '/', intents = intents)

@bot.event
async def on_ready(): # syncing command tree
    try:
        await bot.tree.sync()
        print("synced command tree", bot.tree.get_commands())
    except:
        print("couldn't sync commands")
    
    print(f"logged in as {bot.user}")
    print("Pronto per essere usato, slash commands sincronizzati..") 

async def bot_main():   # MAIN COROUTINE 
    async with bot:  
        # always remember not to start the bot before loading extensions, since its going to block the start of the bot initially
        await bot.load_extension('cogs.music')
        await bot.start(token)
        
if __name__ == "__main__": 
    asyncio.run(bot_main()) #running main coroutine




    




