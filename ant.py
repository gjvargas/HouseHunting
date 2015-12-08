import random

class Ant:
    def __init__(self, uid, nests):
        self.uid = uid
        self.oldNest = nests[0]
        nests[0].addAnt(self)
        self.nest = random.choice(nests[1:])
        self.location = self.nest
        self.active = (self.nest.getQuality() == 1)
        self.recruitable = False 
        self.timeToLocation = 1

    def step(self):
        self.active = (self.nest.getQuality() == 1)
        if self.timeToLocation > 0:
            self.timeToLocation -= 1
        if self.timeToLocation == 0:
            self.location.addAnt(self)
            if self.location.uid == 0:
                self.recruitable = True
            else:
                self.departForNest(1, self.oldNest)

    def recruit(self, colonySize):
        if self.timeToLocation == 0 and self.location.uid == 0 and self.active and (random.random() < (1.0 * self.nest.getPopulation() / colonySize)):
            recruitee = self.location.recruit(self.uid)
            pair = [recruitee, self]
            for ant in pair:
                ant.recruitable = False
                ant.departForNest(1, self.nest)

    def departForNest(self, distance, nest):
        self.oldNest.removeAnt(self)
        self.timeToLocation = distance
        self.location = nest

