from ant import *
import random

class Colony:
    def __init__(self, size, numNests):
        self.ants = [Ant(i) for i in range(size)]
        self.size = size
        self.nests = [Nest(random.randInt(0,1) for i in range(numNests)]

    def step(self):
        for ant in self.ants:
            ant.step()

    def run(self):
        while(True):
            self.step()

    def search(self):
        for ant in self.ants:
            ant.search()

