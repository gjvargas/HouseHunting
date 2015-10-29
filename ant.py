class Ant:
    def __init__(self, uid):
        self.uid = uid

    def step(self):
        print "I am ant number " + str(self.uid)
