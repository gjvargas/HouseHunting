from colony import *
import pickle

def main():
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
    

if __name__ == "__main__":
    main()
