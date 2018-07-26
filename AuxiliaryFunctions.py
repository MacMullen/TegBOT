from CountryClass import *
from TegClass import *
from PlayerClass import *
from DataInit import *


def searchInCountries(listOfCountries, country):
    for j in listOfCountries:
        if (j.name == country):
            return

    print("Not a valid country")
