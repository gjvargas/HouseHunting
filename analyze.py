import pickle
import matplotlib.pyplot as plt

def main():
    results = pickle.load(open("results.p", "r"))
    ants = []
    nests = []
    steps = []
    print("starting loop")
    for result in results:
        ants.append(result["ants"])
        nests.append(result["nests"])
        steps.append(result["steps"])
    print("no infinite loop here")
    plt.plot(ants, steps)
    plt.show()
    print("done")

    

if __name__ == "__main__":
    main()
