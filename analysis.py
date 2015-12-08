import pickle
import numpy as np
import matplotlib.pyplot as plt

def aggregate_data(numTrials, numTests):
	ants = np.zeros((numTrials, numTests))
	nests = np.zeros((numTrials, numTests))
	steps = np.zeros((numTrials, numTests))
	best_qualities = np.zeros((numTrials, numTests))
	chosen_nests = np.zeros((numTrials, numTests),dtype =np.dtype(object))

	for i in range(numTrials):
		data = pickle.load(open('results/ants' + str(i) + '.p','rb'))
		for j in range(len(data)):
			ants[i][j] = data[j]["ants"]
			nests[i][j] = data[j]["nests"]
			steps[i][j] = data[j]["steps"]
			best_qualities[i][j] = data[j]["best_quality"]
			chosen_nests[i][j] = data[j]["chosen"]

	return ants, nests, steps, best_qualities, chosen_nests

def plot_data():
	ants, nests, steps = aggregate_data(30,20)
	m = np.median(steps, axis = 0)
	x = ants[1,:]
	plt.plot(x, m)
	plt.show()

