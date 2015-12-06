import pickle
import matplotlib.pyplot as plt
import numpy as np

def main():
    median_steps = np.zeros(20)
    ants = np.zeros((30, 20))
    nests = np.zeros((30, 20))
    steps = np.zeros((30, 20))
    for i in range(30):
        results = pickle.load(open("results/ants" + str(i) + ".p", "r"))
        count = 0
        for result in results:
            ants[i][count] = result["ants"]
            nests[i][count] = result["nests"]
            steps[i][count] = result["steps"]
            count += 1

    count = 0
    for i in steps.transpose():
        median_steps[count] = sorted(i)[15]
        count += 1

    plt.plot(ants[0], median_steps)
    plt.show()

    

if __name__ == "__main__":
    main()
