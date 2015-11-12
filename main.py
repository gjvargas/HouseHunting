from colony import *

def main():
    colony = Colony(100, 10)
    for i in range(10):
        print 'round ' + str(i)
        colony.step()

if __name__ == "__main__":
    main()
