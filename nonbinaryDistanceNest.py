from sets import Set
from ant import *
from tandemAnt import *
from nest import *
import random

class NonbinaryDistanceNest(Nest):
    def __init__(self, uid):
        self.uid = uid
        self.ants = Set([])
        self.quality = random.randint(0, 1)
        if self.uid == 0:
            self.quality = 0
        self.distance = random.randint(0, 5)
