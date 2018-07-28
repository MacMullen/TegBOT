import pickle
from pathlib import Path

from CountryClass import *


def initCountryStruct():
    dataFile = Path("./data.bin")
    if not dataFile.is_file():
        print("Generating map data...")
        listOfCountries = set([])

        # We define each country name and continent. Then, we add the to our list of countries
        Argentina = Country("Argentina", "SA")
        listOfCountries.add(Argentina)

        Bolivia = Country("Bolivia", "SA")
        listOfCountries.add(Bolivia)

        Chile = Country("Chile", "SA")
        listOfCountries.add(Chile)

        Paraguay = Country("Paraguay", "SA")
        listOfCountries.add(Paraguay)

        Uruguay = Country("Uruguay", "SA")
        listOfCountries.add(Uruguay)

        Brazil = Country("Brasil", "SA")
        listOfCountries.add(Brazil)

        Venezuela = Country("Venezuela", "SA")
        listOfCountries.add(Venezuela)

        Colombia = Country("Colombia", "SA")
        listOfCountries.add(Colombia)

        Nicaragua = Country("Nicaragua", "CA")
        listOfCountries.add(Nicaragua)

        ElSalvador = Country("El Salvador", "CA")
        listOfCountries.add(ElSalvador)

        Honduras = Country("Honduras", "CA")
        listOfCountries.add(Honduras)

        Mexico = Country("Mexico", "CA")
        listOfCountries.add(Mexico)

        Cuba = Country("Cuba", "CA")
        listOfCountries.add(Cuba)

        Jamaica = Country("Jamaica", "CA")
        listOfCountries.add(Jamaica)

        California = Country("California", "NA")
        listOfCountries.add(California)

        Florida = Country("Florida", "NA")
        listOfCountries.add(Florida)

        LasVegas = Country("Las Vegas", "NA")
        listOfCountries.add(LasVegas)

        Chicago = Country("Chicago", "NA")
        listOfCountries.add(Chicago)

        Oregon = Country("Oregon", "NA")
        listOfCountries.add(Oregon)

        Terranova = Country("Terranova", "NA")
        listOfCountries.add(Terranova)

        Canada = Country("Canada", "NA")
        listOfCountries.add(Canada)

        Alaska = Country("Alaska", "NA")
        listOfCountries.add(Alaska)

        VictoriaIsland = Country("Isla Victoria", "NA")
        listOfCountries.add(VictoriaIsland)

        Labrador = Country("Labrador", "NA")
        listOfCountries.add(Labrador)

        NewYork = Country("Nueva York", "NA")
        listOfCountries.add(NewYork)

        Greenland = Country("Groenlandia", "NA")
        listOfCountries.add(Greenland)

        Iceland = Country("Islandia", "EU")
        listOfCountries.add(Iceland)

        Ireland = Country("Irlanda", "EU")
        listOfCountries.add(Ireland)

        UK = Country("Gran Bretaña", "EU")
        listOfCountries.add(UK)

        Portugal = Country("Protugal", "EU")
        listOfCountries.add(Portugal)

        Spain = Country("España", "EU")
        listOfCountries.add(Spain)

        France = Country("Francia", "EU")
        listOfCountries.add(France)

        Germany = Country("Alemania", "EU")
        listOfCountries.add(Germany)

        Italy = Country("Italia", "EU")
        listOfCountries.add(Italy)

        Croatia = Country("Croacia", "EU")
        listOfCountries.add(Croatia)

        Serbia = Country("Serbia", "EU")
        listOfCountries.add(Serbia)

        Poland = Country("Polonia", "EU")
        listOfCountries.add(Poland)

        Albania = Country("Albania", "EU")
        listOfCountries.add(Albania)

        Ukraine = Country("Ucrania", "EU")
        listOfCountries.add(Ukraine)

        Belarus = Country("Bielorrusia", "EU")
        listOfCountries.add(Belarus)

        Finland = Country("Finlandia", "EU")
        listOfCountries.add(Finland)

        Norway = Country("Noruega", "EU")
        listOfCountries.add(Norway)

        Sahara = Country("Sahara", "AFR")
        listOfCountries.add(Sahara)

        Egypt = Country("Egipto", "AFR")
        listOfCountries.add(Egypt)

        Ethiopia = Country("Etiopia", "AFR")
        listOfCountries.add(Ethiopia)

        Nigeria = Country("Nigeria", "AFR")
        listOfCountries.add(Nigeria)

        Angola = Country("Angola", "AFR")
        listOfCountries.add(Angola)

        Mauritania = Country("Mauritania", "AFR")
        listOfCountries.add(Mauritania)

        SouthAfrica = Country("Sudafrica", "AFR")
        listOfCountries.add(SouthAfrica)

        Madagascar = Country("Madagascar", "AFR")
        listOfCountries.add(Madagascar)

        Sumatra = Country("Sumatra", "OCE")
        listOfCountries.add(Sumatra)

        Philippines = Country("Filipinas", "OCE")
        listOfCountries.add(Philippines)

        Tonga = Country("Tonga", "OCE")
        listOfCountries.add(Tonga)

        Australia = Country("Australia", "OCE")
        listOfCountries.add(Australia)

        Tasmania = Country("Tasmania", "OCE")
        listOfCountries.add(Tasmania)

        NewZealand = Country("Nueva Zelandia", "OCE")
        listOfCountries.add(NewZealand)

        Irak = Country("Irak", "ASIA")
        listOfCountries.add(Irak)

        Israel = Country("Israel", "ASIA")
        listOfCountries.add(Israel)

        Arabia = Country("Arabia", "ASIA")
        listOfCountries.add(Arabia)

        Turkey = Country("Turquia", "ASIA")
        listOfCountries.add(Turkey)

        Iran = Country("Iran", "ASIA")
        listOfCountries.add(Iran)

        Russia = Country("Rusia", "ASIA")
        listOfCountries.add(Russia)

        China = Country("China", "Asia")
        listOfCountries.add(China)

        Chechnya = Country("Chechenia", "ASIA")
        listOfCountries.add(Chechnya)

        Siberia = Country("Siberia", "ASIA")
        listOfCountries.add(Siberia)

        Chukchi = Country("Chukchi", "ASIA")
        listOfCountries.add(Chukchi)

        India = Country("India", "ASIA")
        listOfCountries.add(India)

        Malaysia = Country("Malasia", "ASIA")
        listOfCountries.add(Malaysia)

        Korea = Country("Corea", "ASIA")
        listOfCountries.add(Korea)

        Vietnam = Country("Vietnam", "ASIA")
        listOfCountries.add(Vietnam)

        Japon = Country("Japon", "ASIA")
        listOfCountries.add(Japon)

        Kamtchatka = Country("Kamtchatka", "ASIA")
        listOfCountries.add(Kamtchatka)

        # We now define each country neighbours.
        Argentina.neighbours = set([Chile, Bolivia, Paraguay, Uruguay])
        Chile.neighbours = set([Australia, Argentina, Bolivia, Colombia, Brazil])
        Bolivia.neighbours = set([Chile, Argentina, Brazil, Paraguay])
        Paraguay.neighbours = set([Bolivia, Argentina, Brazil])
        Uruguay.neighbours = set([Argentina, Brazil, Nigeria])
        Brazil.neighbours = set([Venezuela, Colombia, Chile, Bolivia, Paraguay, Uruguay, Sahara])
        Colombia.neighbours = set([Chile, Brazil, Venezuela, Nicaragua])
        Venezuela.neighbours = set([Brazil, Colombia])

        Nicaragua.neighbours = set([Colombia, ElSalvador, Jamaica])
        ElSalvador.neighbours = set([Nicaragua, Honduras])
        Honduras.neighbours = set([Cuba, ElSalvador, Mexico])
        Mexico.neighbours = set([Cuba, California, Honduras])
        Cuba.neighbours = set([Mexico, Florida, Honduras, Jamaica])
        Jamaica.neighbours = set([Nicaragua, Cuba])

        California.neighbours = set([Mexico, Tonga, Florida, LasVegas])
        Florida.neighbours = set([California, LasVegas, Chicago, Cuba])
        LasVegas.neighbours = set([Oregon, Chicago, Florida, California])
        Oregon.neighbours = set([Canada, LasVegas, Terranova, Chicago])
        Chicago.neighbours = set([Florida, LasVegas, Oregon, Terranova, NewYork])
        Terranova.neighbours = set([Canada, Oregon, Chicago, Labrador])
        Canada.neighbours = set([Alaska, Oregon, Terranova, VictoriaIsland])
        NewYork.neighbours = set([Greenland, Chicago])
        Labrador.neighbours = set([Terranova, Greenland])
        Greenland.neighbours = set([VictoriaIsland, Labrador, NewYork])
        VictoriaIsland.neighbours = set([Canada, Greenland])
        Alaska.neighbours = set([Canada, Chukchi, Kamtchatka])

        Sahara.neighbours = set([Brazil, Nigeria, Ethiopia, Egypt, Spain])
        Nigeria.neighbours = set([Sahara, Uruguay, Ethiopia, Angola, Mauritania, SouthAfrica])
        Ethiopia.neighbours = set([Egypt, Sahara, Nigeria, Angola])
        Egypt.neighbours = set([Sahara, Ethiopia, Poland, Irak, Israel, Madagascar])
        Angola.neighbours = set([Mauritania, Ethiopia, Nigeria])
        Mauritania.neighbours = set([Angola, Madagascar, SouthAfrica, Nigeria])
        SouthAfrica.neighbours = set([Mauritania, Nigeria, Madagascar])
        Madagascar.neighbours = set([SouthAfrica, Mauritania, Egypt])

        NewZealand.neighbours = set([Tasmania])
        Tasmania.neighbours = set([NewZealand, Australia])
        Australia.neighbours = set([Chile, Tonga, Philippines, Tasmania, Sumatra])
        Tonga.neighbours = set([California, Philippines, Australia])
        Philippines.neighbours = set([Vietnam, Tonga, Australia])
        Sumatra.neighbours = set([Australia, India])

        India.neighbours = set([Vietnam, Malaysia, China, Turkey])
        Vietnam.neighbours = set([India, Malaysia, Korea, Philippines])
        Malaysia.neighbours = set([Vietnam, India, China, Korea])
        Korea.neighbours = set([Japon, Kamtchatka, China, Malaysia])
        China.neighbours = set([Turkey, India, Malaysia, Korea, Kamtchatka, Chukchi, Siberia, Chechnya, Russia])
        Kamtchatka.neighbours = set([Korea, Japon, China, Alaska, Chukchi])
        Japon.neighbours = set([Korea, Kamtchatka])
        Chukchi.neighbours = set([Alaska, Kamtchatka, China])
        Chechnya.neighbours = set([Siberia, Russia, China])
        Siberia.neighbours = set([Chechnya, Russia, China])
        Russia.neighbours = set([China, Chechnya, Siberia, Turkey, Iran, Ukraine])
        Iran.neighbours = set([Russia, Ukraine, Albania, Irak, Turkey])
        Turkey.neighbours = set([China, India, Israel, Irak, Iran, Russia])
        Israel.neighbours = set([Turkey, Arabia, Irak, Egypt])
        Arabia.neighbours = set([Israel])
        Irak.neighbours = set([Egypt, Israel, Turkey, Iran, Albania])

        Albania.neighbours = set([Irak, Iran, Ukraine, Poland])
        Ukraine.neighbours = set([Belarus, Poland, Albania, Iran, Russia])
        Belarus.neighbours = set([Ukraine, Poland, Finland])
        Finland.neighbours = set([Belarus, Norway])
        Norway.neighbours = set([Finland, Iceland])
        Iceland.neighbours = set([Norway, Ireland, Greenland])
        Ireland.neighbours = set([Iceland, UK])
        UK.neighbours = set([Ireland, Germany, Portugal])
        Portugal.neighbours = set([UK, Spain])
        Spain.neighbours = set([Portugal, Sahara, France])
        France.neighbours = set([Spain, Germany, Italy])
        Germany.neighbours = set([UK, France, Italy, Croatia, Serbia, Poland])
        Italy.neighbours = set([France, Germany, Croatia])
        Croatia.neighbours = set([Italy, Germany, Serbia, Poland])
        Serbia.neighbours = set([Poland, Croatia, Germany])
        Poland.neighbours = set([Serbia, Germany, Croatia, Albania, Ukraine, Belarus, Egypt])

        # Let's create different sets for the continents
        NACountries = set([])
        SACountries = set([])
        CACountries = set([])
        EUCountries = set([])
        AFRCountries = set([])
        ASIACountries = set([])
        OCECountries = set([])

        for i in listOfCountries:
            if (i.continent == "NA"):
                NACountries.add(i)
            if (i.continent == "SA"):
                SACountries.add(i)
            if (i.continent == "CA"):
                CACountries.add(i)
            if (i.continent == "EU"):
                EUCountries.add(i)
            if (i.continent == "AFR"):
                AFRCountries.add(i)
            if (i.continent == "ASIA"):
                ASIACountries.add(i)
            if (i.continent == "OCE"):
                OCECountries.add(i)
        # Save the initial structure of the game in a binary file.
        with open('./data.bin', 'wb') as filehandle:
            pickle.dump(
                [listOfCountries, NACountries, SACountries, CACountries, EUCountries, AFRCountries, ASIACountries,
                 OCECountries], filehandle)
    else:
        print("Loading map data...")
        with open('./data.bin', 'rb') as filehandle:
            # Read the data as binary data stream
            listOfCountries, NACountries, SACountries, CACountries, EUCountries, AFRCountries, ASIACountries, OCECountries = pickle.load(
                filehandle)

    return listOfCountries, NACountries, SACountries, CACountries, EUCountries, AFRCountries, ASIACountries, OCECountries


def initMissionList():
    return []
