from ant import *

class Colony:
    def __init__(self, size, numNests):
        self.ants = []
        self.size = size
        self.nests = []
        for i in range(numNests):

        self.nests = nests
        for i in range(size):
            self.ants.append(Ant(i))

    def step(self):
        for ant in self.ants:
            ant.step()

    def run(self):
        while(True):
            self.step()

    def search(self):
        for ant in self.ants:
            ant.search()

