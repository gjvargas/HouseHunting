from sets import Set
from ant import *
from tandemAnt import *
import random

class Nest:
    def __init__(self, uid):
        self.uid = uid
        self.ants = Set([])
        self.quality = random.randint(0,1)
        if self.uid == 0:
            self.quality = 0
        self.distance = 1

    def addAnt(self, ant):
        if self.uid != 0:
            ant.nest.removeAnt(ant)
            ant.nest = self
        self.ants.add(ant)

    def removeAnt(self, ant):
        self.ants.discard(ant)

    def getPopulation(self):
        return len(self.ants)

    def getQuality(self):
        return self.quality

    def recruit(self, recruiterUid):
        assert self.uid == 0
        ants = list(self.ants)
        if len(ants) > 1:
            output = random.choice(list(self.ants))
            while (output == recruiterUid):
                output = random.choice(list(self.ants))
            return output
