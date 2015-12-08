import cPickle as pickle
import matplotlib.pyplot as plt
import numpy as np

def aggregateData(numTrials, numTests, folder):
    ants = np.zeros((numTrials,numTests))
    nests = np.zeros((numTrials,numTests))
    steps = np.zeros((numTrials,numTests))
    bestQualities = np.zeros((numTrials,numTests))
    chosenNests = np.zeros((numTrials,numTests),dtype=object)
    for i in range(numTrials):
        data = pickle.load(open(folder+"/ants"+str(i)+".p","r"))
        for j in range(len(data)):
            ants[i][j] = data[j]["ants"]
            nests[i][j] = data[j]["nests"]
            steps[i][j] = data[j]["steps"]
            bestQualities[i][j] = data[j]["bestQuality"]
            chosenNests[i][j] = data[j]["chosenNest"]
    return ants,nests,steps,bestQualities,chosenNests

def plotSteps(ants,controlSteps,nonbinarySteps):
    x = ants[1,:]
    controlMedian = np.median(controlSteps,axis=0)
    nonbinaryMedian = np.median(nonbinarySteps,axis=0)

    control, = plt.plot(x,controlMedian,label="control")
    nonbinary, = plt.plot(x,nonbinaryMedian,label="nonbinary")
    plt.legend([control,nonbinary],["Control","Nonbinary"])
    plt.show()

def plotChosenQualities(ants,controlChosenNests,controlBestQualities,nonbinaryChosenNests,nonbinaryBestQualities):
    x = ants[1,:]
    def extractQuality(nest):
        return nest.quality
    vfunc = np.vectorize(extractQuality)

    controlChosenQualities = vfunc(controlChosenNests)
    nonbinaryChosenQualities = vfunc(nonbinaryChosenNests)

    controlMedian = np.median((controlChosenQualities-controlBestQualities)/controlBestQualities,axis=0)
    nonbinaryMedian = np.median((nonbinaryChosenQualities-nonbinaryBestQualities)/nonbinaryBestQualities,axis=0)
    
    control, = plt.plot(x,controlMedian,label="control")
    nonbinary, = plt.plot(x,nonbinaryMedian,label="nonbinary")
    legend = plt.legend([control,nonbinary],['control','nonbinary'])
    plt.show()