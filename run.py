from colony import *
import pickle
import sys
from ant import Ant
from tandemAnt import TandemAnt
from nest import Nest
from distanceNest import DistanceNest
from nonbinaryDistanceNest import NonbinaryDistanceNest

def main(argv):
    numTrials = int(argv[0])
    numAnts = int(argv[1])
    numNests = int(argv[2])
    antType = eval(argv[3])
    nestType = eval(argv[4])    


    output = []
    for i in range(numTrials):
        # print("Starting Trial", i)
        colony = Colony(numAnts, numNests, antType, nestType)
        numSteps, bestQuality, chosenNest = colony.go()
        dataPoint = {"ants": numAnts, "nests": numNests, "steps": numSteps, \
            "bestQuality": bestQuality, "chosenNest": chosenNest, "trial": i}
        output.append(dataPoint)
        # print("Finished Trial", i)
    pickle.dump(output, open(argv[4][:-4] + "Results/" + str(numAnts) + "ants.p", "w"))

if __name__ == "__main__":
    main(sys.argv[1:])
