import pickle
import matplotlib.pyplot as plt
import numpy as np

def aggregateData(numTrials, numTests):
    ants = np.zeros((numTrials,numTests))
    nests = np.zeros((numTrials,numTests))
    steps = np.zeros((numTrials,numTests))
    bestQualities = np.zeros((numTrials,numTests))
    chosenNests = np.zeros((numTrials,numTests),dtype=object)
    for i in range(numTrials):
        data = pickle.load(open("results/ants"+str(i)+".p","rb"))
        for j in range(len(data)):
            ants[i][j] = data[j]["ants"]
            nests[i][j] = data[j]["nests"]
            steps[i][j] = data[j]["steps"]
            bestQualities[i][j] = data[j]["bestQuality"]
            chosenNests[i][j] = data[j]["chosenNest"]
    return ants,nests,steps,bestQualities,chosenNests

def plot_steps():
    ants,nests,steps,bestQualities,chosenNests=aggregateData(30,20)
    x = ants[1,:]
    y = np.median(steps,axis=0)
    plt.plot(x,y)
    plt.show()

def plot_chosenQualities():
    ants,nests,steps,bestQualities,chosenNests=aggregateData(30,20)
    x = ants[1,:]
    def extractQuality(nest):
        return nest.quality
    vfunc = np.vectorize(extractQuality)
    chosenQualities = vfunc(chosenNests)
    y = np.median((chosenQualities-bestQualities)/bestQualities,axis=0)
    plt.plot(x,y)
    plt.show()