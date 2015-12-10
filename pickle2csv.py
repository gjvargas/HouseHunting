import pickle
import os
import sys

def main(argv):
    d = argv[0]

    csv = open("ResultsCSV/" + d[:-1] + ".csv", "w")

    for f in os.listdir(d):
        pickleFile = open(d + f, "rb")
        trials = pickle.load(pickleFile)
        for t in trials:
            csv.write(str(t['ants']) + ',' + str(t['steps']) + ',' + \
            str(t['bestQuality']) + ',' + str(t['chosenNest'].quality) + \
            ',' + str(t['chosenNest'].distance) + ',' + str(t['nests']) + \
            '\n')
        pickleFile.close()
        
    csv.close()

if __name__ == "__main__":
    main(sys.argv[1:])
