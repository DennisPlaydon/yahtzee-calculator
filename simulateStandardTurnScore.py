from engine import yahtzeeEngine
import time
import statistics
import sys

# I was curious what a standard roll looks like. 
# Often I end up with 3 of the same value in a 3 turn yahtzee set of rolls.
# This will simulate what the median and average scores are. 

# A score of 4 represents four of the same dice.
def averageStandardScoreSimulation(runs: int):
    total_list = []
    total = 0
    for i in range(runs):
        score = getAverageRollCount()
        total_list.append(score)
        total += score

    print("========== Results ==========")
    print("Median score after 3 rolls:", statistics.median(total_list))
    print("Average score after 3 rolls:", total/runs)

def getAverageRollCount():
    final = yahtzeeEngine.standardTurn()

    countMostFrequent, _ = yahtzeeEngine.mostFrequent(final)

    return countMostFrequent

if __name__ == "__main__":
    numberOfRuns = 1000
    if len(sys.argv) > 1:
        try:
            numberOfRuns = int(sys.argv[1])
        except ValueError:
            pass
        
    start_time = time.time()
    print("Starting simulation...")
    averageStandardScoreSimulation(numberOfRuns)

    print("\n========== Additional information ==========")
    print("Program finished in %s seconds" % (time.time() - start_time))
    print("Simulations:", numberOfRuns)