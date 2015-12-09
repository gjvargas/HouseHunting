import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pickle
import os

d = "ControlResults/"

dataframe = pd.DataFrame()
dataframe['ants'] = []
dataframe['steps'] = []

#csv = open("ControlResults/results.csv", "a")

for f in os.listdir(d):
    trials = pickle.load(open(d + f, "rb"))
    ants = []
    steps = []
    for t in trials:
        #csv.write(str(t['ants']) + ',' + str(t['steps']) + ',' + str(t['bestQuality']) + ',' + str(t['chosenNest'].quality) + ',' + str(t['chosenNest'].distance))
        ants.append(t['ants'])
        steps.append(t['steps'])
    df = pd.DataFrame()
    df['ants'] = ants
    df['steps'] = steps
    dataframe = dataframe.append(df)
    
    print dataframe

sns.regplot("ants", "steps", dataframe, logx=True)
#g = sns.FacetGrid(dataframe)
#g.map(plt.scatter, "ants", "steps", marker="o", alpha=.3)

sns.plt.show()
