import discord

from discord import app_commands
from discord.ext import commands
import logging
from dotenv import load_dotenv # library to put tokens, passwords, api keys etc.
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.all()     # Specify all bots intents(all because idk what i actually have to give him)

bot = commands.Bot(command_prefix = '/', intents = intents) 

# get the voice channel in which the user calling the command is connected, make bot play audio

@bot.event
async def on_ready():
    print("Pronto per essere usato, slash commands sincronizzati..")
    await bot.tree.sync()


@bot.tree.command(name="audio")
async def audio(interaction):

    try:
        voice = discord.utils.get(bot.voice_clients, guild=interaction.guild) # This allows for more functionality with voice channels

        if voice == None: # None being the default value if the bot isnt in a channel (which is why the is_connected() is returning errors)
            await interaction.response.send_message("<@" + str(interaction.user.id) + ">" + " mi sto connettendo...")
            await interaction.user.voice.channel.connect()
            
        else:
            await interaction.response.send_message("sono già connesso, dovrei mettere la musica direttamente ma non lo so fare...")
    except:
        
        await interaction.response.send_message("<@" + str(interaction.user.id) + ">" + " Non sei connesso a nessun canale oppure c'è stato un errore")

    pass

bot.run(token)