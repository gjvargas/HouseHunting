import pickle
import numpy, scipy.io 

for i in range(30):
	data=pickle.load(open("results/ants" + str(i) + ".p", "rb"))
	scipy.io.savemat('results/ants'+str(i)+'.mat', mdict={'data': data})
