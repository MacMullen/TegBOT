class Player:
    def __init__(self, name, color, mission):
        self.name = name
        self.color = color
        self.countries = set([])
        self.mission = mission
        self.human = True

    def convertToBOT(self):
        self.human = False

    def addCountry(self, country):
        self.countries.add(country)

    def changeColor(self, newColor):
        self.color = newColor
