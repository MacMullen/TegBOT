import random
from main import *

from CountryClass import *
from TegClass import *
from PlayerClass import *
from DataInit import *


def initPlayerContries(player):
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


def getCountryByName(country):
    for c in listOfCountries:
        if country == c.name:
            return c
        else:
            print("That country doesn't exists")


def raffleExtraCountries():
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


def selectMission():
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
        p.mission = int(input())


def firstTurn():
    print("Throw the dices to establish who starts first on the first round")
    first_turn = input("Who won?")
    first_turn_index = 0
    for p in listOfPlayers:
        assert isinstance(p, Player)
        if first_turn == p.name:
            p.turn = 0
            next_turn = 1
            while True:
                playerNextTo(p).turn = next_turn
                next_turn = next_turn + 1
                p = playerNextTo(p)
                if p.name == first_turn:
                    break


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


def countriesFrom(continent, countries: set[Country]):
    sum = 0
    for c in countries:
        if c.continent == continent:
            sum = sum + 1

    return sum


def playerGotSixIslands(countries: set[Country]):
    return True


def playerWithColor(color):
    for p in listOfPlayers:
        if p.color == color:
            return p


def playerToTheRight(player):
    assert isinstance((player, Player))
    player_index = listOfPlayers.index(player)
    if player_index == 0:
        return listOfPlayers[len(listOfPlayers) - 1]
    else:
        return listOfPlayers[player_index - 1]


def playerNextTo(player):
    assert isinstance((player, Player))
    player_index = listOfPlayers.index(player)
    if player_index != (len(listOfPlayers) - 1):
        return listOfPlayers[player_index + 1]
    else:
        return listOfPlayers[0]


def checkMissionCompletition(player: Player):
    mission_index = player.mission
    if mission_index == 1:
        if EUCountries.issubset(player.countries) and SACountries.issubset(player.countries):
            print("{} wins!".format(player.name))
    if mission_index == 2:
        if NACountries.issubset(player.countries) and OCECountries.issubset(player.countries) and (
                countriesFrom("AFR", player.countries) == 5):
            print("{} wins!".format(player.name))
    if mission_index == 3:
        if ASIACountries.issubset(player.countries) and CACountries.issubset(player.countries):
            print("{} wins!".format(player.name))
    if mission_index == 4:
        if NACountries.issubset(player.countries) and (countriesFrom("ASIA", player.countries) == 8) and (
                countriesFrom("EU", player.countries) == 4):
            print("{} wins!".format(player.name))
    if mission_index == 5:
        if (countriesFrom("NA", player.countries) == 4) and (countriesFrom("EU", player.countries) == 4) and (
                countriesFrom("ASIA", player.countries) == 4) and (countriesFrom("SA", player.countries) == 3) and (
                countriesFrom("CA", player.countries) == 3) and (countriesFrom("AFR", player.countries) == 3) and (
                countriesFrom("OCE", player.countries) == 3):
            print("{} wins!".format(player.name))
    if mission_index == 6:
        if OCECountries.issubset(player.countries) and (countriesFrom("ASIA", player.countries) == 6) and (
                countriesFrom("AFR", player.countries) == 6) and (countriesFrom("NA", player.countries) == 6):
            print("{} wins!".format(player.name))
    if mission_index == 7:
        if CACountries.issubset(player.countries) and (countriesFrom("SA", player.countries) == 6) and (
                countriesFrom("EU", player.countries) == 6) and (countriesFrom("ASIA", player.countries) == 6):
            print("{} wins!".format(player.name))
    if mission_index == 8:
        if SACountries.issubset(player.countries) and AFRCountries.issubset(player.countries) and (
                countriesFrom("ASIA", player.countries) == 8):
            print("{} wins!".format(player.name))
    if mission_index == 9:
        if OCECountries.issubset(player.countries) and AFRCountries.issubset(player.countries) and (
                countriesFrom("CA", player.countries) == 4) and (countriesFrom("ASIA", player.countries) == 4):
            print("{} wins!".format(player.name))
    if mission_index == 10:
        if EUCountries.issubset(player.countries) and (countriesFrom("SA", player.countries) == 4) and (
                countriesFrom("ASIA", player.countries) == 4):
            print("{} wins!".format(player.name))
    if mission_index == 11:
        if AFRCountries.issubset(player.countries) and (countriesFrom("EU", player.countries) == 4) and (
                countriesFrom("ASIA", player.countries) == 4) and playerGotSixIslands(player.countries):
            print("{} wins!".format(player.name))
    if mission_index == 12:
        if len(player.countries) == 35:
            print("{} wins!".format(player.name))
    if mission_index == 13:
        if "White" not in listOfColors:
            if len(playerWithColor("White").countries) == 0:
                print("{} wins!".format(player.name))
        else:
            if len(playerToTheRight(player).countries) == 0:
                print("{} wins!".format(player.name))
    if mission_index == 14:
        if "Black" not in listOfColors:
            if len(playerWithColor("Black").countries) == 0:
                print("{} wins!".format(player.name))
        else:
            if len(playerToTheRight(player).countries) == 0:
                print("{} wins!".format(player.name))
    if mission_index == 15:
        if "Red" not in listOfColors:
            if len(playerWithColor("Red").countries) == 0:
                print("{} wins!".format(player.name))
        else:
            if len(playerToTheRight(player).countries) == 0:
                print("{} wins!".format(player.name))
    if mission_index == 16:
        if "Blue" not in listOfColors:
            if len(playerWithColor("Blue").countries) == 0:
                print("{} wins!".format(player.name))
        else:
            if len(playerToTheRight(player).countries) == 0:
                print("{} wins!".format(player.name))
    if mission_index == 17:
        if "Yellow" not in listOfColors:
            if len(playerWithColor("Yellow").countries) == 0:
                print("{} wins!".format(player.name))
        else:
            if len(playerToTheRight(player).countries) == 0:
                print("{} wins!".format(player.name))
    if mission_index == 18:
        if "Green" not in listOfColors:
            if len(playerWithColor("Green").countries) == 0:
                print("{} wins!".format(player.name))
        else:
            if len(playerToTheRight(player).countries) == 0:
                print("{} wins!".format(player.name))
    if mission_index == 19:
        for p in listOfPlayers:
            if len(playerNextTo(p).countries) == 0:
                print("{} wins!".format(player.name))
    if len(player.countries) == 45:
        print("{} wins!".format(player.name))


def attackPhase(p):
    assert isinstance(p, Player)
    conquered = 0
    while True:
        print("Do you want to attack?")
        print("1. Yes")
        print("2. No")
        want_to_attack = int(input())
        if want_to_attack == 2:
            return conquered
        else:
            conquered = conquered + attackCountry(p)


def attackCountry(p):
    print("Which country do you want to attack:")
    i = 1
    for c in p.countries:
        for k in c.neighbours:
            if k.owner != p.name:
                print("{}. {}".format(i, k.name))
                i += 1
    country_to_attack = input()
    print("With what country do you want to attack {}".format(country_to_attack))
    country_to_attack = getCountryByName(country_to_attack)
    i = 1
    for c in country_to_attack.neighbours:
        if c.owner == p.name:
            print("{}. {}".format(i, c.name))
            i += 1
    attack_from_country = input()
    attack_from_country = getCountryByName(attack_from_country)
    print("Roll Dices...")
    print("Result for attacker:")
    attacker_dices = []
    if attack_from_country.playerChips == 1:
        first_dice = int(input())
        attacker_dices.append(first_dice)
    if attack_from_country.playerChips == 2:
        first_dice = int(input())
        second_dice = int(input())
        attacker_dices.append(first_dice)
        attacker_dices.append(second_dice)
    if attack_from_country.playerChips >= 3:
        first_dice = int(input())
        second_dice = int(input())
        third_dice = int(input())
        attacker_dices.append(first_dice)
        attacker_dices.append(second_dice)
        attacker_dices.append(third_dice)
    attacker_dices.sort()
    defender_dices = []
    if country_to_attack.playerChips == 1:
        first_dice = int(input())
        defender_dices.append(first_dice)
    if country_to_attack.playerChips == 2:
        first_dice = int(input())
        second_dice = int(input())
        defender_dices.append(first_dice)
        defender_dices.append(second_dice)
    if country_to_attack.playerChips >= 3:
        first_dice = int(input())
        second_dice = int(input())
        third_dice = int(input())
        defender_dices.append(first_dice)
        defender_dices.append(second_dice)
        defender_dices.append(third_dice)
    defender_dices.sort()
    attacker_lost_chips = 0
    defender_lost_chips = 0
    while len(defender_dices) > len(attacker_dices) or len(attacker_dices) > len(defender_dices):
        if len(defender_dices) > len(attacker_dices):
            defender_dices.pop()
        if len(defender_dices) < len(attacker_dices):
            attacker_dices.pop()
    for x in range(len(attacker_dices)):
        if attacker_dices[x] > defender_dices[x]:
            defender_lost_chips += 1
        else:
            attacker_lost_chips += 1
    attack_from_country.loseChips(attacker_lost_chips)
    country_to_attack.loseChips(defender_lost_chips)
    if country_to_attack.playerChips <= 0:
        country_to_attack.owner = attack_from_country.owner
        print("How many chips are going to reinforce {}".format(country_to_attack.name))
        amount_of_chips = input(">>")
        country_to_attack.addReinforcements(amount_of_chips)
        return 1
    return 0


def regroupPhase(p):
    print("Do you want to move chips?")
    print("1. Yes")
    print("2. No")
    want_to_regroup = int(input())
    if want_to_regroup == 2:
        return
    assert isinstance(p, Player)
    print("From which country do you want to move chips?")
    country_from = input()
    country_from = getCountryByName(country_from)
    i = 1
    for c in p.countries:
        print("{}. {}".format(i, c.name))
        i += 1
    print("To which country do you want to move chips?")
    i = 1
    for c in country_from.neighbours:
        if c.owner == p.name:
            print("{}. {}".format(i, c.name))
            i += 1
    country_to = input()
    country_to = getCountryByName(country_to)
    print("How many chips?")
    amount = input()
    country_from.loseChips(amount)
    country_to.addReinforcements(amount)
    print("Done")


def withdrawCard(p):
    assert isinstance(p, Player)
    print("Withdraw a card")
    print("Which country is it?")
    card_country = input()
    card_country = getCountryByName(card_country)
    if card_country in p.countries:
        card_country.addReinforcements(3)
    print("What type of card is it?")
    print("1. Soldier")
    print("2. Plane")
    print("3. Anchor")
    print("4. Supercard")
    type_of_card = int(input())
    p.cardWithdrawn.add(type_of_card)


def nextTurn():
    for p in listOfPlayers:
        if p.turn == 0:
            p.turn = playerToTheRight(p).turn
        else:
            p.turn -= 1
    sorted(listOfPlayers, key=lambda p_turn: p.turn)
    for p in listOfPlayers:
        amount = int(len(p.countries) / 2)
        reinforceCountries(p, amount)
