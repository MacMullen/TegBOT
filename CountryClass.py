class Country:
    def __init__(self, name, continent):
        self.name = name
        self.continent = continent
        self.playerChips = 1
        self.owner = 0
        self.neighbours = 0

    def changeOwner(self, newOwner, amountChips):
        self.owner = newOwner
        self.playerChips = amountChips

    def loseChips(self, amountChips):
        self.playerChips = self.playerChips - amountChips

    def addReinforcements(self, amountChips):
        self.playerChips = self.playerChips + amountChips
