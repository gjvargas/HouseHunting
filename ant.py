import random

class Ant:
    def __init__(self, uid, nest):
        self.uid = uid
        self.nest = nest
        self.active = True
        self.recruited = False
        self.travelling = 0

    def step(self):
    	self.travelling = max(self.travelling-1, 0)

