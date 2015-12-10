import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import pandas as pd
import pickle
import os
import sys

def main(argv):
    d = argv[0]
    dataframe = pd.DataFrame()
    dataframe['Number of Ants'] = []
    dataframe['Number of Steps'] = []

    for f in os.listdir(d):
        ants = []
        steps = []

        csv = open(d + f, "rb")
        for line in csv:
            trial = [x.strip() for x in line.split(',')]
            print trial
            ants.append(int(trial[0]))
            steps.append(int(trial[2]))
        
        csv.close()
        df = pd.DataFrame()
        df['Number of Ants'] = ants
        df['Number of Steps'] = steps
        dataframe = dataframe.append(df)

    print dataframe

    mpl.rcParams['xtick.labelsize'] = 20
    mpl.rcParams['ytick.labelsize'] = 20 
    #g = sns.regplot('Number of Ants', 'Number of Steps', dataframe, logx=True, hue='Nest Distance')    
    g = sns.lmplot('Number of Ants', 'Number of Steps', dataframe, logx=True)
    g.set(xlim=(0,2050))
    g.set(ylim=(0,160))
    font = {'fontname':'Arial','size':'30'}
    plt.xlabel('Number of Ants',**font)
    plt.ylabel('Number of Steps',**font)

    sns.plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])
