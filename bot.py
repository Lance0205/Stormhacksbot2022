import discord
from discord.ext import commands

TOKEN = 'OTQ0NzYzMDExNjE1MzE4MDY3.YhGVHg.IOOPn_Y9nPzAtZS2YQJbc5qZuys

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def ping():
    await client.say('Pong!')

client.run(TOKEN)