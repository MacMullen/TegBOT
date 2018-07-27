import pickle
from pathlib import Path
from pick import pick

from CountryClass import *
from TegClass import *
from PlayerClass import *
from DataInit import *
from AuxiliaryFunctions import *

# Initialize the map of game.
listOfCountries, NACountries, SACountries, CACountries, EUCountries, AFRCountries, ASIACountries, OCECountries = initCountryStruct()

# Initialize the list of possible colors.
listOfColors = ["Green", "Yellow", "Blue", "White", "Black", "Red"]

# Initialize an empty list for the players
listOfPlayers = []

# Let's ask how many players are going to play
while True:
    numberOfPlayers = int(input("How many players are going to play? "))
    if (numberOfPlayers > 6):
        print("Too many players")
    else:
        break

while True:
    numberOfBots = int(input("How many BOTS do you want to add to the game? "))
    if (numberOfBots > 6 - numberOfPlayers):
        print("Too many BOTS")
    else:
        break

# Calculate how many countries each player start with
amountOfInitialCountries = int(len(listOfCountries) / (numberOfPlayers + numberOfBots))
amountOfExtraCountries = len(listOfCountries) % (numberOfPlayers + numberOfBots)
print("Each player will start with {} countries".format(amountOfInitialCountries))
print("There are {} countries to raffle between players".format(amountOfExtraCountries))
title = 'How do you want to raffle the countries: '
options = ['Dices', 'Random']
option, index = pick(options, title)
print(option)
print(index)

for i in range(numberOfPlayers):
    name = input("What is the name of player {}? ".format(i))
    while True:
        color = input("What color do you want to use? ")
        if (color not in listOfColors):
            print("Wrong color")
        else:
            break
    listOfColors.remove(color)

    mission = input("What is your mission? ")
    # (TODO)Make the player select his mission from a list.
    player = Player(name, color, mission)

    print("Which countries are you starting with? ")
    initPlayerContries(amountOfInitialCountries, listOfCountries, player)

    listOfPlayers.append(player)

# Now, let's setup the bots
for i in range(numberOfBots):
    name = "BOT_{}".format(i)
    color = listOfColors[0]
    listOfColors.remove(listOfColors[0])

    mission = input("Which is BOT_{} mission? ".format(i))
    player = Player(name, color, mission)

    print("Which countries is BOT_{} starting with?".format(i))
    initPlayerContries(amountOfInitialCountries, listOfCountries, player)

    player.convertToBOT()
    listOfPlayers.append(player)
