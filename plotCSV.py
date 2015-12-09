import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pickle
import os
import sys

def main(argv):
    filename = argv[0]
    dataframe = pd.DataFrame()
    f = open(filename, 'rb')

    ants = []
    steps = []

    for line in f:
        trial = [x.strip() for x in line.split(',')]
        ants.append(int(trial[0]))
        steps.append(int(trial[1]))

    dataframe['ants'] = ants
    dataframe['steps'] = steps

    print dataframe

    sns.regplot('ants', 'steps', dataframe, logx=True).set(xlim=(0,2050))
    sns.plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])
