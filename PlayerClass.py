class Player:
    def __init__(self, name, color, startingCountries):
        self.name = name
        self.color = color
        self.countries = startingCountries
        self.mission = 0

    def addMission(self, mission):
        self.mission = mission

    def changeColor(self, newColor):
        self.color = newColor
