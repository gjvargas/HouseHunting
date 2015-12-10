from colony import *
import pickle
import sys
from ant import Ant
from tandemAnt import TandemAnt
from nest import Nest
from distanceNest import DistanceNest
from nonbinaryDistanceNest import NonbinaryDistanceNest
import os

def main(argv):
    numTrials = int(argv[0])
    numAnts = int(argv[1])
    numNests = int(argv[2])
    antType = eval(argv[3])
    nestType = eval(argv[4])    

    filename = argv[3] + argv[4] + "Thres100/" + argv[1] + argv[3] + argv[2] + argv[4] + ".csv"
    if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
    csv = open(filename, "w")
    for i in range(numTrials):
        colony = Colony(numAnts, numNests, antType, nestType)
        numSteps, bestQuality, chosenNest = colony.go()
        csv.write( \
            str(numAnts) + ',' + \
            str(numNests) + ',' + \
            str(numSteps) + ',' + \
            str(bestQuality) + ',' + \
            str(chosenNest.quality) + ',' + \
            str(chosenNest.distance) + '\n' \
        )
    csv.close()

if __name__ == "__main__":
    main(sys.argv[1:])
