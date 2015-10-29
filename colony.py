from ant import *

class Colony:
    def __init__(self, size):
        self.ants = []
        self.size = size
        for i in range(size):
            self.ants.append(Ant(i))

    def step(self):
        for ant in self.ants:
            ant.step()

    def run(self):
        while(True):
            self.step()
