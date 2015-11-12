from ant import *
from nest import *
import random
import copy

class Colony:
    def __init__(self, size, numNests):
        self.nests = [Nest(i, random.randint(0,1)) for i in range(numNests)]
        self.ants = [Ant(i, random.choice(self.nests[1:])) for i in range(size)]
        for ant in self.ants:
            ant.nest.addAnt(ant)
        self.size = size

    def step(self):
        recruitingAnts = []
        for ant in self.ants:
            ant.recruited = False
            ant.active = (ant.nest.quality == 1)
            if ant.active and (random.random() < (ant.nest.getPopulation() / self.size)):
                recruitingAnts.append(ant)
        pairs = self.recruit(recruitingAnts)
        for ant in pairs:
            recruitedAnt = pairs[ant]
            recruitedAnt.nest.removeAnt(ant)
            recruitedAnt.nest = ant.nest
            ant.nest.addAnt(recruitedAnt)
            recruitedAnt.active = True
        print [nest.getPopulation() for nest in self.nests]



    def recruit(self, recruitingAnts):
        pairs = {}
        permutation = copy.copy(self.ants)
        random.shuffle(permutation)
        for ant in permutation:
            if ant in recruitingAnts and not ant.recruited:
                recruitedAnt = random.choice(self.ants)
                if not recruitedAnt.recruited:
                    recruitedAnt.recruited
                    pairs[ant] = recruitedAnt
        return pairs

        
        


    def run(self):
        while(True):
            self.step()
