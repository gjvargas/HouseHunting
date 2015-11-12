import random

class Ant:
    def __init__(self, uid, nest):
        self.uid = uid
        self.nest = nest
        self.active = True
        self.recruited = False
