import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
#intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


# Événement qui se déclenche lorsque le bot est prêt
@bot.event
async def on_ready():
    print(f'Bot {bot.user} est connecté.')


# Commande simple "ping"
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Salut {ctx.author.mention}!')


token = os.getenv("DISCORD_TOKEN")
bot.run(token)
