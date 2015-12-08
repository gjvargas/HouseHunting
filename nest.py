from ant import *

class Nest:
    def __init__(self, uid, quality, distance):
        self.uid = uid
        self.ants = []
        self.quality = quality
        self.distance = distance

    def addAnt(self, ant):
        self.ants.append(ant)

    def removeAnt(self, ant):
        self.ants.remove(ant)

    def getPopulation(self):
        return len(self.ants)

    def getQuality(self):
        return self.quality

    def getDistance(self):
        return self.distance
