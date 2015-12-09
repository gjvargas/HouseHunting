import random
GUIDANCE_SLOWDOWN = 3

class Ant:
    def __init__(self, uid, nests):
        self.uid = uid
        self.oldNest = nests[0]
        nests[0].addAnt(self)
        self.nest = random.choice(nests[1:])
        self.location = self.nest
        self.active = (random.random() < self.nest.getQuality())
        self.recruitable = False 
        self.timeToLocation = self.nest.distance

    def step(self):
        self.active = (random.random() < self.nest.getQuality())
        if self.timeToLocation > 0:
            self.timeToLocation -= 1
        if self.timeToLocation == 0:
            self.location.addAnt(self)
            if self.location.uid == 0:
                self.recruitable = True
            else:
                self.returnToOldNest()

    def shouldTandemRun(self, colonySize):
        return False

    def recruit(self, colonySize):
        if self.timeToLocation == 0 and self.location.uid == 0 and self.active and (random.random() < (1.0 * self.nest.getPopulation() / colonySize)):
            recruitee = self.location.recruit(self.uid)
            if recruitee is not None:
                if (self.shouldTandemRun(colonySize)):
                    self.carryToNest(recruitee)
                else:
                    self.guideToNest(recruitee)

    def guideToNest(self, recruitee):
        self.oldNest.removeAnt(self)
        recruitee.oldNest.removeAnt(recruitee)
        
        global GUIDANCE_SLOWDOWN
        self.timeToLocation = self.nest.distance * GUIDANCE_SLOWDOWN
        recruitee.timeToLocation = self.nest.distance * GUIDANCE_SLOWDOWN

        self.location = self.nest
        recruitee.location = self.nest

    def carryToNest(self, recruitee):
        self.oldNest.removeAnt(self)
        recruitee.oldNest.removeAnt(recruitee)

        if recruitee.nest != self.nest:
            recruitee.oldNest = None

        self.timeToLocation = self.nest.distance
        recruitee.timeToLocation = self.nest.distance

        self.location = self.nest
        recruitee.location = self.nest

    def returnToOldNest(self):
        if self.oldNest:
            self.timeToLocation = self.nest.distance
            self.location = self.oldNest
