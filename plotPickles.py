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
    dataframe['ants'] = []
    dataframe['steps'] = []

    for f in os.listdir(d):
        pickleFile = open(d + f, "rb")
        trials = pickle.load(pickleFile)
        ants = []
        steps = []
        for t in trials:
            ants.append(t['ants'])
            steps.append(t['steps'])
        df = pd.DataFrame()
        df['ants'] = ants
        df['steps'] = steps
        dataframe = dataframe.append(df)
        
        print dataframe
        pickleFile.close()

    sns.regplot("ants", "steps", dataframe, logx=True).set(xlim=(0,2050))
    sns.plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])
