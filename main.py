from colony import *
import pickle
import sys
from ant import Ant
from tandemAnt import TandemAnt
from nest import Nest

def main(argv):
    numTrials = int(argv[0])
    numAnts = int(argv[1])
    numNests = int(argv[2])
    antType = eval(argv[3])
    nestType = eval(argv[4])    
    
    for x in range(numTrials):
        print 'starting trial', x
        trials = [(i, numNests) for i in range(50, numAnts+1, 50)]
        output = []
        for numAnts, numNests in trials:
            print("starting trial", numAnts, numNests)
            colony = Colony(numAnts, numNests, antType, nestType)
            numSteps, bestQuality, chosenNest = colony.go()
            dataPoint = {"ants": numAnts, "nests": numNests, "steps": numSteps,\
                "bestQuality": bestQuality, "chosenNest": chosenNest}
            output.append(dataPoint)
            print("just finished trial", numAnts, numNests)
        pickle.dump(output, open("results/ants" + str(x) + ".p", "w"))
        print 'finished trial', x
    

if __name__ == "__main__":
    main(sys.argv[1:])
