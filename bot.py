import asyncio
import discord
import os
from discord.ext import commands


# Token_Discord est une variable d'environement contenant le token discord du bot
TOKEN = os.getenv('Token_Discord')

# Intents requis pour que le bot fonctionne
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Créez une instance de bot
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    # Ignore les messages envoyés par le bot lui-même
    if message.author == bot.user:
        return

    # Mot ou phrase à rechercher
    trigger_word = 'hello'

    # path to the file
    file_path = "Bot_Discord/téléchargement.jpg"
    
    if trigger_word in message.content.lower():
        await message.channel.send(f'Hello, {message.author.mention}!', file=discord.File(file_path))

    # Permet au bot de traiter les commandes (si vous avez des commandes définies)
    await bot.process_commands(message)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Lancez le bot
bot.run(TOKEN)