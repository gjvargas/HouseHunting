from nonbinary import *
import pickle
import numpy, scipy.io

def main():
    for x in range(30):
    	print 'started', x
        trials = [(i * 50, 20) for i in range(1, 21)]
        output = []
        for numAnts, numNests in trials:
            # print("starting trial", numAnts, numNests)
            colony = Colony(numAnts, numNests)
            numSteps, chosen_quality, best_quality = colony.go()
            dataPoint = {"ants": numAnts, "nests": numNests, "steps": numSteps, "chosen": chosen_quality, "best": best_quality}
            output.append(dataPoint)
            # print("just finished trial", numAnts, numNests)
        scipy.io.savemat('resultsMat/ants'+str(i)+'.mat', mdict={'data': output})
        pickle.dump(output, open("results/ants" + str(x) + ".p", "w"))
        print 'finished', x

if __name__ == "__main__":
    main()
