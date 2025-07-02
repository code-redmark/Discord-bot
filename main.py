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

    audio = discord.FFmpegPCMAudio("https://cdn.freecodecamp.org/curriculum/js-music-player/scratching-the-surface.mp3")

    try:
        voice = discord.utils.get(bot.voice_clients, guild=interaction.guild)
        if voice == None: # if there are no voice clients in the interactions guild...
            await interaction.response.send_message("<@" + str(interaction.user.id) + ">" + " mi connetto..")
            await interaction.user.voice.channel.connect()
            discord.utils.get(bot.voice_clients, guild=interaction.guild).play(audio)

        elif voice.channel != interaction.user.voice.channel:  # Move to user channel if already connected
             await voice.move_to(interaction.user.voice.channel)
             discord.utils.get(bot.voice_clients, guild=interaction.guild).play(audio)
        else:
             discord.utils.get(bot.voice_clients, guild=interaction.guild).play(audio)

    except:   
            await interaction.response.send_message("<@" + str(interaction.user.id) + ">" + " Non sei connesso a nessun canale oppure c'è stato un errore")
            
            pass

bot.run(token)