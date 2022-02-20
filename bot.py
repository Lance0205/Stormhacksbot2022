import discord
from discord.ext import commands

TOKEN = ''

client = commands.bot(command_prefix = '!')

@client.event
async