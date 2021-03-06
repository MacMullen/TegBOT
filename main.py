from DataInit import *
from AuxiliaryFunctions import *

# Initialize the map of game.
listOfCountries, NACountries, SACountries, CACountries, EUCountries, AFRCountries, ASIACountries, OCECountries = initCountryStruct()

# Initialize the list of possible colors.
listOfColors = ["Green", "Yellow", "Blue", "White", "Black", "Red"]

# Initialize an empty list for the players
listOfPlayers = []

# Initiliaze the modifiers
snow = False
tailwind = False
crisis = False
extra_reinforcements = False
open_borders = False
closed_borders = False
rest = False
globalSituations = [snow, tailwind, crisis, extra_reinforcements, open_borders, closed_borders, rest]

# Let's ask how many players are going to play
while True:
    numberOfPlayers = int(input("How many players are going to play? "))
    if numberOfPlayers > 6:
        print("Too many players")
    else:
        break

# Let's ask how many BOTS are going to play
while True:
    numberOfBots = int(input("How many BOTS do you want to add to the game? "))
    if numberOfBots > 6 - numberOfPlayers:
        print("Too many BOTS")
    else:
        break

# Calculate how many countries each player start with
amountOfInitialCountries = int(len(listOfCountries) / (numberOfPlayers + numberOfBots))
amountOfExtraCountries = len(listOfCountries) % (numberOfPlayers + numberOfBots)
print("Each player will start with {} countries".format(amountOfInitialCountries))

for i in range(numberOfPlayers):
    name = input("What is the name of player {}? ".format(i + 1))
    while True:
        color = input("What color do you want to use? ")
        if color not in listOfColors:
            print("Wrong color")
        else:
            break
    listOfColors.remove(color)

    player = Player(name, color)

    print("Which countries are you starting with? ")
    initPlayerCountries(player, amountOfInitialCountries, listOfCountries)

# Now, let's setup the bots
for i in range(numberOfBots):
    name = "BOT_{}".format(i)
    color = listOfColors[0]
    listOfColors.remove(listOfColors[0])

    bot = Player(name, color)

    print("Which countries is BOT_{} starting with?".format(i))
    initPlayerCountries(bot, amountOfInitialCountries, listOfCountries)

    bot.convertToBOT()
    listOfPlayers.append(bot)

# Raffle the extra countries.
if amountOfExtraCountries != 0:
    raffleExtraCountries(listOfCountries, amountOfExtraCountries, listOfPlayers)

# Now  we define each player mission
selectMission(listOfPlayers)

# Establish the first turn order of players
firstTurn(listOfPlayers)
sorted(listOfPlayers, key=lambda player_turn: player.turn)

# First turn of reinforcements
for p in listOfPlayers:
    reinforceCountries(p, 8)
for p in listOfPlayers:
    reinforceCountries(p, 4)

# Begin the game
while True:
    pickSituationCard(globalSituations)
    for p in listOfPlayers:
        if not p.human:
            i = 0
            # TODO: Develop BOT Intelligence
        else:
            conquered = attackPhase(p, listOfCountries)
            regroupPhase(p, listOfCountries)
            if conquered:
                withdrawCard(p, listOfCountries)
    nextTurn(listOfPlayers)
