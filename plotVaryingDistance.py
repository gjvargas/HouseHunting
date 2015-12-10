import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import pandas as pd
import pickle
import os
import sys

def main():
	folders = ['AntNest','AntDistanceNest','TandemAntDistanceNest']
	antTypes = ['Ant','Ant','TandemAnt']
	nestTypes = ['Nest','DistanceNest','DistanceNest']
	medians = np.zeros((len(folders),40))
	ants = np.ones((len(folders),1))*np.array(range(50,2001,50))
	for k in range(len(folders)):
		folder = folders[k]
		antType = antTypes[k]
		nestType = nestTypes[k]
		steps = np.zeros((50,40))
		for i in range(40):
			numAnts = (i+1)*50
			filename = 'Results/'+folder+'/'+str(numAnts)+antType+'20'+nestType+'.csv'
			f = open(filename,'rb')
			j = 0
			for line in f:
				trial = [x.strip() for x in line.split(',')]
				if(len(trial[0])==0): break
				steps[j][i] = int(trial[2])
				j += 1
		medians[k,:] = np.median(steps,axis=0)

	medians[0,:] = 3 * medians[0,:]
	mpl.rcParams['xtick.labelsize'] = 20
	mpl.rcParams['ytick.labelsize'] = 20  
	sns.set_style('darkgrid')
	lines = plt.plot(ants.transpose(),medians.transpose())
	names = ['Ant with Constant Distance Nests', \
		'Ant with Varying Distance Nests',\
		'Direct Transport Ant with Varying Distance Nests']
	plt.legend(lines, names,loc='upper left')
	font = {'fontname':'Arial', 'size':'30'}
	plt.xlabel('Number of Ants',**font)
	plt.ylabel('Number of Steps',**font)
	plt.show()

if __name__ == "__main__":
	main()