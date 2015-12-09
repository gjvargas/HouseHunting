from sets import Set
from ant import *
from tandemAnt import *
from nest import *
import random

class DistanceNest(Nest):
    def __init__(self, uid):
        self.uid = uid
        self.ants = Set([])
        self.quality = 1
        if self.uid == 0:
            self.quality = 0
        self.distance = random.randint(1, 5)
