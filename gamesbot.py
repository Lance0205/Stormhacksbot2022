#topic: animals, countries

animalsRead = open("animals.txt",'r',encoding="utf-8")
animals = {}

for quote in animalsRead:
    animal = animal.strip()
    animals.append(animal)

countriesRead = open("countries.txt",'r',encoding="utf-8")
countries = {}

for country in countriesRead:
    country = country.strip()
    countries.append(country)

