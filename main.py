import discord 
from discord.ext import commands
from random import randint
import os 
from dotenv import load_dotenv

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


bot.run(os.getenv("DISCORD_TOKEN"))