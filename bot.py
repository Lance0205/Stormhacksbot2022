import discord
import random

quoteOpen = open("quotes.txt",'r',encoding="utf-8")
quotes = []

for quote in quoteOpen:
    quote = quote.strip()
    quotes.append(quote)

print(quotes)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!inspire me'):
        await message.channel.send(random.choice(quotes))

client.run('OTQ0NzYzMDExNjE1MzE4MDY3.YhGVHg.IOOPn_Y9nPzAtZS2YQJbc5qZuys')