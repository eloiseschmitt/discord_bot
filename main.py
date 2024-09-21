import discord
from discord.ext import commands

# Initialisation du bot avec un préfixe "!" pour les commandes
bot = commands.Bot(command_prefix='!')


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


# Lancer le bot avec le token
bot.run(DISCORD_TOKEN)
