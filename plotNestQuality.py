import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import pandas as pd
import pickle
import os
import sys

def main():
	folders = ['AntNest','AntNonbinaryNest',\
		'AntNonbinaryDistanceNest','TandemAntNonbinaryNest',\
		'TandemAntNonbinaryDistanceNest']
	antTypes = ['Ant','Ant','Ant',\
		'TandemAnt','TandemAnt']
	nestTypes = ['Nest',\
		'NonbinaryNest','NonbinaryDistanceNest',\
		'NonbinaryNest','NonbinaryDistanceNest']
	medians = np.zeros((len(folders),40))
	ants = np.ones((len(folders),1))*np.array(range(50,2001,50))
	for k in range(len(folders)):
		folder = folders[k]
		antType = antTypes[k]
		nestType = nestTypes[k]
		chosenQualities = np.zeros((50,40))
		bestQualities = np.zeros((50,40))
		for i in range(40):
			numAnts = (i+1)*50
			filename = 'Results/'+folder+'/'+str(numAnts)+antType+'20'+nestType+'.csv'
			f = open(filename,'rb')
			j = 0
			for line in f:
				trial = [x.strip() for x in line.split(',')]
				if(len(trial[0])==0): break
				bestQuality = float(trial[3])
				chosenQuality = float(trial[4])
				bestQualities[j][i] = bestQuality
				chosenQualities[j][i] = chosenQuality
				j += 1
		medians[k,:] = np.median((bestQualities-chosenQualities)/bestQualities,axis=0)

	mpl.rcParams['xtick.labelsize'] = 20
	mpl.rcParams['ytick.labelsize'] = 20  
	sns.set_style('darkgrid')
	lines = plt.plot(ants.transpose(),medians.transpose())
	names = ['Ant with Normal Nest', 'Ant with Non-binary Nest',\
		'Ant with Non-binary Nest and Varying Distance',\
		'Direct Transport Ant with Non-binary Nest',\
		'Direct Transport Ant with Non-binary Nest and Varying Distance']
	plt.legend(lines, names,loc='upper right')
	font = {'fontname':'Arial', 'size':'30'}
	plt.xlabel('Number of Ants',**font)
	plt.ylabel('Number of Steps',**font)
	plt.show()

if __name__ == "__main__":
    main()