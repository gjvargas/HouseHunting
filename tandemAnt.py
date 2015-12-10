import random
from ant import Ant

class TandemAnt(Ant):
    def shouldTandemRun(self, colonySize):
        populationProportion = 1.0 * self.nest.getPopulation() / colonySize
        return populationProportion > 1 and random.random() < populationProportion ** 2
