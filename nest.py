from ant import *

class Nest:
    def __init__(self, quality):
        self.ants = []
        self.quality = quality

    def addAnt(self, ant):
        self.ants.append(ant)

    def getPopulation(self):
        return len(self.ants)

    def getQuality(self):
        return self.quality
