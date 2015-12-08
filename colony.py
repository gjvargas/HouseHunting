from ant import *
from nest import *
import random
import copy

class Colony:
    def __init__(self, size, numNests):
        self.nests = [Nest(i) for i in range(numNests)]
        self.ants = [Ant(i, self.nests) for i in range(size)]
        for ant in self.ants:
            ant.nest.addAnt(ant)
        self.size = size

    def step(self):
        for ant in self.ants:
            ant.step()
            ant.recruit(self.size)

    def go(self):
        count = 0
        while self.size not in [nest.getPopulation() for nest in self.nests[1:]]:
            print [nest.getPopulation() for nest in self.nests]
            count += 1
            self.step()
        print [nest.getPopulation() for nest in self.nests]
        return count
