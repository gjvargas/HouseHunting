import random
import copy
from ant import *
from tandemAnt import *
from nest import *
from nonbinaryNest import *

class Colony:
    def __init__(self, size, numNests, antType, nestType):
        numNests += 1 # don't count home nest
        self.nests = [nestType(i) for i in range(numNests)]
        while all([nest.quality == 0 for nest in self.nests]):
            self.nests = [nestType(i) for i in range(numNests)]

        self.ants = [antType(i, self.nests) for i in range(size)]
        for ant in self.ants:
            ant.nest.addAnt(ant)
        self.size = size

    def step(self):
        random.shuffle(self.ants)
        for ant in self.ants:
            ant.step()
        for ant in self.ants:
            ant.recruit(self.size)

    def go(self):
        count = 0
        best_quality = max([nest.quality for nest in self.nests])
        while self.size not in [nest.getPopulation() for nest in self.nests[1:]]:
            #print [nest.getPopulation() for nest in self.nests]
            count += 1
            self.step()
        #print [nest.getPopulation() for nest in self.nests]
        chosen_nest = [nest for nest in self.nests if nest.getPopulation() == self.size][0]
        return count, best_quality, chosen_nest
