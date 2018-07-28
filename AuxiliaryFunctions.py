import random

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


def raffleExtraCountries(listOfCountries, listOfPlayers):
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
            winner = random.randint(0, len(playersInRaffle) - 1)
            print("{} won {}".format(playersInRaffle[winner].name, extraCountries[x].name))
            playersInRaffle[winner].countries.add(extraCountries[x])
            extraCountries[x].owner = playersInRaffle[winner].name
            playersInRaffle.remove(winner)
        del playersInRaffle
    del extraCountries


def selectMission(listOfPlayers, missionList):
    for p in listOfPlayers:
        print("What is {} mission? ".format(p.name))
        print("1. Ocupar Europa y America del Sur")
        print("2. Ocupar America del Norte, Oceania y 5 paises de Africa")
        print("3. Ocupar Asia y America Central")
        print("4. Ocupar America del Norte, 8 paises de Asia y 4 de Europa")
        print("5. Ocupar 4 paises de America del Norte, 4 de Europa, 4 de Asia, 3 de America del Sur, 3 de America "
              "Central, 3 de Africa y 3 de Oceania")
        print("6. Ocupar Oceania, 6 paises de Asia, 6 de Africa y 6 de America del Norte")
        print("7. Ocupar America Central, 6 paises de America del Sur, 6 de Europa y 6 de Asia")
        print("8. Ocupar America del Sur, Africa y 8 paises de Asia")
        print("9. Ocupar OCeania, Africa, 4 paises de America Central y 4 de Asia")
        print("10. Ocupar Europa, 4 paises de Asia y 4 paises de America del Sur")
        print(
            "11. Ocupar Africa, 4 paises de Europa, 4 paises de Asia y 6 islas, repartidas en por lo menos 3 continentes")
        print("12. Ocupar 35 paises en cualquier lugar del mapa")
        print("13. Destruir al ejercito Blanco; de ser imposible, al jugador de la derecha")
        print("14. Destruir al ejercito Negro; de ser imposible, al jugador de la derecha")
        print("15. Destruir al ejercito Rojo; de ser imposible, al jugador de la derecha")
        print("16. Destruir al ejercito Azul; de ser imposible, al jugador de la derecha")
        print("17. Destruir al ejercito Amarillo; de ser imposible, al jugador de la derecha")
        print("18. Destruir al ejercito Verde; de ser imposible, al jugador de la derecha")
        print("19. Destruir al jugador de la izquierda")
        mission_index = int(input())
        p.mission = missionList[mission_index - 1]


def firstTurn(listOfPlayers):
    print("Throw the dices to establish who starts first on the first round")
    first_turn = input("Who won?")
    first_turn_index = 0
    for p in listOfPlayers:
        if first_turn == p.name:
            first_turn_index = listOfPlayers.index(p)
            break
    for p in listOfPlayers:
        p.turn = listOfPlayers.index(p) - first_turn_index


def reinforceCountries(player, n):
    while True:
        if n == 0:
            break
        else:
            country = input("Where do you want to reinforce your army?")
            amount = input("How many chips do you want to add? ({} remaining)".format(n))
            for c in player.countries:
                if country == c.name:
                    c.addReinforcements(amount)
                    n = n - amount
