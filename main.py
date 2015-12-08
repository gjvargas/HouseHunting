from colony import *
import pickle
import sys
from ant import Ant
from tandemAnt import TandemAnt
from nest import Nest

def main(argv):
    numAnts = int(argv[0])
    numNests = int(argv[1])
    antType = eval(argv[2])
    nestType = eval(argv[3])
    colony = Colony(numAnts, numNests, antType, nestType)
    numSteps = colony.go()
    print numSteps
    
    '''
    for x in range(30):
        trials = [(i * 50, 20) for i in range(1, 21)]
        output = []
        for numAnts, numNests in trials:
            print("starting trial", numAnts, numNests)
            colony = Colony(numAnts, numNests)
            numSteps = colony.go()
            dataPoint = {"ants": numAnts, "nests": numNests, "steps": numSteps}
            output.append(dataPoint)
            print("just finished trial", numAnts, numNests)
        pickle.dump(output, open("ants" + str(x) + ".p", "w"))
    '''

if __name__ == "__main__":
    main(sys.argv[1:])
