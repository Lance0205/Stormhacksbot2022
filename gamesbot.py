#topic: animals, countries

import random

animalsRead = open("animals.txt",'r',encoding="utf-8")
animals = {}

for animal in animalsRead:
    animal = animal.strip()
    animal = animal.split(",")
    animals[animal[0]] = animal[1:]

countriesRead = open("countries.txt",'r',encoding="utf-8")
countries = {}

for country in countriesRead:
    country = country.strip()
    country = country.split(",")

userInput = input("Chose your theme (animals, countries, etc): ")

if userInput == "animals":
    items = random.choice(list(animals.items()))

    keyword = items[0]

    hint = items[1]

elif userInput == "countries":
    items = random.choice(list(countries.items()))

    keyword = items[0]

    hint = items[1]

for guess in range(6):
    userGuess = input("Enter your guess ({}): ".format(userInput))

    displayGuess = ""
    underline = "\u0332"
    #conditions \u0332 
    i=0
    for letter in userGuess:
        if letter in keyword:
            if letter == keyword[i]:
                displayGuess += letter
            else:
                displayGuess += letter
                displayGuess += underline

        else:
            displayGuess += "_"
        i+=1






