from engine import yahtzeeEngine
import sys
import time

# I was curious how many yahtzees you get in a simulation of runs. 
# For example: In a million standard turns - how many are yahtzees.

def numberOfYahtzeesSimulation(runs):
    yahtzees = 0
    for i in range(runs):
        final = yahtzeeEngine.standardTurn()

        if (yahtzeeEngine.isYahtzee(final)):
            yahtzees+=1

    print("========== Results ==========")
    print("Total number of Yahtzees:", yahtzees)

if __name__ == "__main__":
    numberOfRuns = 1000
    if len(sys.argv) > 1:
        try:
            numberOfRuns = int(sys.argv[1])
        except ValueError:
            pass

    start_time = time.time()
    print("Starting simulation...")
    numberOfYahtzeesSimulation(numberOfRuns)

    print("\n========== Additional information ==========")
    print("Program finished in %s seconds" % (time.time() - start_time))
    print("Simulations:", numberOfRuns)