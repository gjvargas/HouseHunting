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
            self.guideToNest(recruitee, 1, self.nest)

    def guideToNest(self, recruitee, distance, nest):
        self.oldNest.removeAnt(self)
        recruitee.oldNest.removeAnt(recruitee)

        self.timeToLocation = distance * 3
        recruitee.timeToLocation = distance * 3

        self.location = nest
        recruitee.location = nest

    def carryToNest(self, recruitee, distance, nest):
        self.oldNest.removeAnt(self)
        recruitee.oldNest.removeAnt(recruitee)

        recruitee.oldNest = None

        self.timeToLocation = distance
        recruitee.timeToLocation = distance

        self.location = nest
        recruitee.location = nest

    def departForNest(self, distance, nest):
        if nest:
            self.oldNest.removeAnt(self)
            self.timeToLocation = distance
            self.location = nest

