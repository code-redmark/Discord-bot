import discord

from discord import app_commands
from discord.ext import commands

import traceback
import asyncio
from yt_dlp import YoutubeDL



class PlaySound(commands.Cog):
    def __init__(self, bot):
         self.bot = bot 

    async def playquery(self, interaction, query):

        ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'default_search': 'ytsearch',
        'noplaylist': True,
        'skip_download': True
    }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(query, download=False)

            # If the query returns a search result or playlist
            if 'entries' in info:
                info = info['entries'][0]  # take first result safely

            stream_url = info.get('url')
            discord.utils.get(self.bot.voice_clients, guild=interaction.guild).play(discord.FFmpegPCMAudio(stream_url))
            if not stream_url:
                await interaction.channel.send(" Could not find a valid stream URL.")
                return

        except Exception as e:
            await interaction.channel.send(f"yt-dlp error: {e}")
        return

         
    @app_commands.command(name="audio", description="non so come cazzo si diamine acciderbolina vez")

    async def connect(self, interaction: discord.Interaction, richiesta: str):
    
        try:

            voice = discord.utils.get(self.bot.voice_clients, guild=interaction.guild)
            await interaction.response.defer()

            if voice == None: # if there are no voice clients in the interactions guild...
                await interaction.user.voice.channel.connect()
                await interaction.followup.send(interaction.user.mention + " mi connetto..")
                await self.playquery(interaction, richiesta)

            elif voice.channel != interaction.user.voice.channel:  # Move to user channel if already connected
                await voice.disconnect()
                await interaction.user.voice.channel.connect()
                await self.playquery(interaction, richiesta)
            else:
                voice.stop()
                await asyncio.sleep(1)
                await interaction.followup.send(interaction.user.mention + " cambio canzone cazzo era bella questa dio cane")
                await self.playquery(interaction, richiesta)

        except Exception as ex:   
                await interaction.followup.send(interaction.user.mention + " Non sei connesso a nessun canale oppure c'è stato un errore")
                ex_channel = discord.utils.get(interaction.guild.channels, name="marco_exception_log") # change name to selected error channel
                ex_msg = traceback.format_exc() # formatting error to send it in channel
                await ex_channel.send(ex_msg)
    
        pass

# REQUIRED function for the bot to load this cog
async def setup(bot: commands.Bot):
    await bot.add_cog(PlaySound(bot))