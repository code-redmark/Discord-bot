import discord

from discord import app_commands
from discord.ext import commands

import traceback
import asyncio
import yt_dlp



class PlaySound(commands.Cog):
    def __init__(self, bot):
         self.bot = bot 

    async def play(self, url):
         ytdlp = yt_dlp.y
         pass

         
    @app_commands.command(name="audio", description="Ciao ciao ciao ciao")

    async def connect(self, interaction: discord.Interaction, link = None):

        audio = discord.FFmpegPCMAudio() # audio to be played
    



        try:

            voice = discord.utils.get(self.bot.voice_clients, guild=interaction.guild)
            await interaction.response.defer()

            if voice == None: # if there are no voice clients in the interactions guild...
                await interaction.user.voice.channel.connect()
                await interaction.followup.send(interaction.user.mention + " mi connetto..")
                discord.utils.get(self.bot.voice_clients, guild=interaction.guild).play(audio)

            elif voice.channel != interaction.user.voice.channel:  # Move to user channel if already connected
                await voice.disconnect()
                await interaction.user.voice.channel.connect()
                discord.utils.get(self.bot.voice_clients, guild=interaction.guild).play(audio)
            else:
                discord.utils.get(self.bot.voice_clients, guild=interaction.guild).stop()
                await asyncio.sleep(1)
                await interaction.followup.send(interaction.user.mention + " sono già connesso, farò ripartire la musica da capo")
                discord.utils.get(self.bot.voice_clients, guild=interaction.guild).play(audio)

        except Exception as ex:   
                await interaction.followup.send(interaction.user.mention + " Non sei connesso a nessun canale oppure c'è stato un errore")
                ex_channel = discord.utils.get(interaction.guild.channels, name="marco_exception_log") # change name to selected error channel
                ex_msg = traceback.format_exc() # formatting error to send it in channel
                await ex_channel.send(ex_msg)
    
        pass

# REQUIRED function for the bot to load this cog
async def setup(bot: commands.Bot):
    await bot.add_cog(PlaySound(bot))