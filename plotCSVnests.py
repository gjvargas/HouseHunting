import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pickle
import os
import sys

def main(argv):
    d = argv[0]
    dataframe = pd.DataFrame()
    dataframe['Number of Nests'] = []
    dataframe['Number of Steps'] = []

    for f in os.listdir(d):
        nests = []
        steps = []

        csv = open(d + f, "rb")
        for line in csv:
            trial = [x.strip() for x in line.split(',')]
            print trial
            nests.append(int(trial[1]))
            steps.append(int(trial[2]))
        
        csv.close()
        df = pd.DataFrame()
        df['Number of Nests'] = nests
        df['Number of Steps'] = steps
        dataframe = dataframe.append(df)

    print dataframe

    #g = sns.regplot('Number of Ants', 'Number of Steps', dataframe, logx=True, hue='Nest Distance')    
    g = sns.lmplot('Number of Nests', 'Number of Steps', dataframe)
    #g.set(xlim=(0,2050))
    #g.set(ylim=(0,160))

    sns.plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])
