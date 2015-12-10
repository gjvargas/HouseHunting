import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pickle
import os
import sys

def main():
	thresholds = [str(t) for t in range(60,101,10)]
	medians = np.zeros((len(thresholds),40))
	ants = np.ones((len(thresholds),1))*np.array(range(50,2001,50))
	for k in range(len(thresholds)):
		t = thresholds[k]
		steps = np.zeros((50,40))
		for i in range(40):
			numAnts = (i+1)*50
			filename = 'TandemAntNestThres'+t+'/'+str(numAnts)+'TandemAnt20Nest.csv'
			f = open(filename,'rb')
			j = 0
			for line in f:
				trial = [x.strip() for x in line.split(',')]
				if(len(trial[0])==0): break
				step = int(trial[2])
				steps[j][i] = step
				j += 1
		medians[k,:] = np.median(steps,axis=0)
	sns.set_style('darkgrid')
	lines = plt.plot(ants.transpose(),medians.transpose())
	plt.legend(lines,['t='+t for t in thresholds],loc='upper left')
	plt.xlabel('Number of Ants')
	plt.ylabel('Number of Steps')
	plt.show()

if __name__ == "__main__":
    main()