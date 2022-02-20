import discord
import random
import time

keyword = ''
guess = 0

#FOR QUOTES
quoteOpen = open("quotes.txt",'r',encoding="utf-8")
quotes = []
for quote in quoteOpen:
    quote = quote.strip()
    quotes.append(quote)



animals = {"dog" : "three","elk" : "
}


countries = {"Canada" : "this is Canada"}

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

@client.event 
async def on_message(message, a = None):
    if message.author == client.user:
        return

    global keyword

    if message.content.startswith('break'):
        await message.channel.send("Lets play Wardle")

        await message.channel.send("Chose your theme (animals, countries, etc): ")
        return 

    if message.content.startswith("animals"): 
        items = random.choice(list(animals.items()))
        keyword = items[0]
        hint = items[1]
        userInput = "animals"
        return
        

    elif message.content.startswith("countries"):
        items = random.choice(list(countries.items()))
        keyword = items[0]
        hint = items[1]
        userInput = "countries"
        return
        
    else:
        global guess
        if guess<6:
            guess += 1
            
            displayGuess = ""
            underline = "\u0332"
            
            i=0
            for letter in message.content:
                if letter in keyword:
                    if letter == keyword[i]:
                        displayGuess += letter
                    else:
                        displayGuess += letter
                        displayGuess += underline

                else:
                    displayGuess += "\_"
        
                i+=1
            await message.channel.send("Result is {}".format(displayGuess))
        

    

client.run('OTQ0NzYzMDExNjE1MzE4MDY3.YhGVHg.IOOPn_Y9nPzAtZS2YQJbc5qZuys')