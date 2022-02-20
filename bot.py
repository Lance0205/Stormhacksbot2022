import discord
from discord.ext import commands

TOKEN = 'OTQ0NDQzMDIwNDU4MjA5MzMw.YhBrGg.MvK4jFnA2VOVJKVWIRji0h9H7Cw'

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def ping():
    await client.say('Pong!')

client.run(TOKEN)