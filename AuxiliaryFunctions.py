from CountryClass import *
from TegClass import *
from PlayerClass import *
from DataInit import *


def initPlayerContries(amountOfInitialCountries, listOfCountries, player):
    for i in range(amountOfInitialCountries):
        country = input()
        while True:
            if (searchInCountries(listOfCountries, country)):
                if (searchInCountries(player.countries, country)):
                    print("Country already in the list.")
                    country = print()
                else:
                    break
            else:
                print("Not a valid country")
                country = input()
        for j in listOfCountries:
            if (j.name == country):
                player.addCountry(j)
                j.owner = player.name

def searchInCountries(listOfCountries, country):
    for j in listOfCountries:
        if (j.name == country):
            return True

    return False
