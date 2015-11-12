import random

class Ant:
    def __init__(self, uid, colonySize, nest):
        self.uid = uid
        self.colonySize = colonySize
        self.nest = nest
        self.active = True

    def step(self):
        

        print "I am ant number " + str(self.uid)

    def search(self, nests):
        self.nest = nests[random.randInt(1, len(nests) - 1)]
        return self.nest
