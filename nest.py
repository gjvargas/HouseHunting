from ant import *
import random

class Nest:
    def __init__(self, uid):
        self.uid = uid
        self.ants = []
        self.quality = random.randint(0,1)
        if self.uid == 0:
            self.quality = 0
        self.distance = 1

    def addAnt(self, ant):
        if ant not in self.ants:
            if self.uid != 0:
                ant.nest.removeAnt(ant)
                ant.nest = self
            self.ants.append(ant)

    def removeAnt(self, ant):
        if ant in self.ants:
            self.ants.remove(ant)

    def getPopulation(self):
        return len(self.ants)

    def getQuality(self):
        return self.quality

    def recruit(self, recruiterUid):
        assert self.uid == 0
        output = random.choice(self.ants)
        while (output == recruiterUid):
            output = random.choice(self.ants)
        return output
