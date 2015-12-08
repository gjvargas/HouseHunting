import random
import copy
from ant import *
from tandemAnt import *
from nest import *
from nonbinaryNest import *

class Colony:
    def __init__(self, size, numNests, antType, nestType):
        self.nests = [nestType(i) for i in range(numNests)]
        self.ants = [antType(i, self.nests) for i in range(size)]
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
