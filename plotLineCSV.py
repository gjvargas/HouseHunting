import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pickle
import os
import sys

def main(argv):
	medians = np.zeros((len(argv),40))
	ants = np.ones((len(argv),1))*np.array(range(50,2001,50))
	for k in range(len(argv)):
		filename = argv[k]
		f = open(filename,'rb')
		steps = np.zeros((50,40))
		trials = np.zeros((1,40))
		for line in f:
			trial = [x.strip() for x in line.split(',')]
			ant = int(trial[0])
			step = int(trial[1])
			j = ant/50-1
			i = trials[0][j]
			steps[i][j] = step
			trials[0][j] += 1
		medians[k,:] = np.median(steps,axis=0)

	sns.set_style('darkgrid')
	plt.plot(ants.transpose(),medians.transpose())
	plt.show()

	
	

if __name__ == "__main__":
    main(sys.argv[1:])
