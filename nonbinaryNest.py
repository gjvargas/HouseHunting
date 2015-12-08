from sets import Set
from ant import *
from tandemAnt import *
from nest import *
import random

class NonbinaryNest(Nest):
    def __init__(self, uid):
        self.uid = uid
        self.ants = Set([])
        self.quality = random.random()
        if self.uid == 0:
            self.quality = 0
        self.distance = 1
