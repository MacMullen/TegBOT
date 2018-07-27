import random

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

for i in range(1, numberOfPlayers):
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
    bot = Player(name, color, mission)

    print("Which countries is BOT_{} starting with?".format(i))
    initPlayerContries(amountOfInitialCountries, listOfCountries, bot)

    bot.convertToBOT()
    listOfPlayers.append(bot)

# Raffle the extra countries.
if amountOfExtraCountries != 0:
    # Build a list with countries that don't have owners.
    extraCountries = []
    for j in listOfCountries:
        if j.owner == 0:
            extraCountries.append(j)
    # Ask how the players want to raffle the countries.
    print("There are {} countries to raffle between players".format(amountOfExtraCountries))
    print("How do you want to raffle the countries:")
    print("1. Dices")
    print("2. Random")
    sel_input = int(input("Select:"))
    if sel_input == 1:
        for i in range(len(extraCountries)):
            print("Roll the dice to win {}".format(extraCountries[i].name))
            winner = input("Who won?")
            for p in listOfPlayers:
                if p.name == winner:
                    p.countries.add(extraCountries[i])
                    extraCountries[i].owner = winner
    if sel_input == 2:
        playersInRaffle = listOfPlayers
        for x in range(len(extraCountries)):
            winner = random.randint(0, len(playersInRaffle))
            print("{} won {}".format(playersInRaffle[winner].name, extraCountries[x].name))
            playersInRaffle[winner].countries.add(extraCountries[x])
            extraCountries[x].owner = playersInRaffle[winner].name
            playersInRaffle.remove(winner)
        del playersInRaffle
    del extraCountries
