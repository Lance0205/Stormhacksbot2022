import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    words = ["You are loved!",
    "You can do this!",
    ""
    random_compliment = random.choice(words)

    if message.content.startswith('help me'):
        await message.channel.send(random_compliment)
    
    
    
    
    ]
    

client.run('OTQ0NzYzMDExNjE1MzE4MDY3.YhGVHg.IOOPn_Y9nPzAtZS2YQJbc5qZuys')