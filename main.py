from random import randint
import os
import logging

from services.youtube.youtube_service import YoutubeService

import discord
from discord.ext import commands
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

youtube = YoutubeService()
load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)
nomes_permitidos = ["briin", "v_tudonumaboa" "alex_r_s"]

@bot.event
async def on_ready():
    print("Bot inicializado com sucesso")

@bot.command()
async def ola(ctx:commands.Context):
    nome = ctx.author.name
    await ctx.reply(f"Olá, {nome}! Tudo bem?")
    print("Comando realizado com sucesso.")

@bot.command()
async def salve(ctx:commands.Context):
    nome = ctx.author.name
    if nome.lower() in nomes_permitidos:
        await ctx.reply(f'Salve meu mano, {ctx.author.nick} vqv vapo!')
    else: 
        await ctx.reply("Sobra nada :P")

@bot.command()
async def switch(ctx:commands.Context):
    roles = ctx.author.roles 
    for role in roles: 
        if role.name == 'teste':
            await ctx.reply("Trocando de canais...")

            return
    await ctx.reply('Você não tem permissão para essa ação.')

@bot.command()
async def play(ctx:commands.Context, query: str):
    if discord.utils.get(ctx.author.roles, name="DJ"):
        try:
            youtube_results = await youtube.search_videos(query, max_results=3)
            message = "**Select one of the results:**\n\n"

            for i, video in enumerate(youtube_results, start=1):
                message += f"- {i}. {str(video)}"

            await ctx.send(message)
        except Exception as e:
            logger.error(f"Error searching YouTube videos: {e}")
            await ctx.send("An error occurred while searching for videos.")
    else:
        await ctx.send("You don't have permission to use this command.")

bot.run(os.getenv("DISCORD_TOKEN"))