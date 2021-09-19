from engine import yahtzeeEngine
import time
import statistics
import sys

# I was curious what it takes to actually get a yahtzee. 
# You may get a yahtzee on the first roll but it might be on the 70th.
# This will output median, average, min and max rolls to get a yahtzee.

def rollsUntilYahtzee(runs):
    numRollsToYahtzeeList = []
    totalSum = 0
    for i in range(runs):
        count = yahtzeeEngine.countRollUntilYahtzee()
        numRollsToYahtzeeList.append(count)
        totalSum += count
    print("========== Results ==========")
    print("Median rolls until Yahtzee:", statistics.median(numRollsToYahtzeeList))
    print("Average rolls until Yahtzee:", totalSum/runs)
    print("Minimum rolls until Yahtzee:", min(numRollsToYahtzeeList))
    print("Maximum rolls until Yahtzee:", max(numRollsToYahtzeeList))

if __name__ == "__main__":
    numberOfRuns = 1000
    if len(sys.argv) > 1:
        try:
            numberOfRuns = int(sys.argv[1])
        except ValueError:
            pass
        
    start_time = time.time()
    print("Starting simulation...")
    rollsUntilYahtzee(numberOfRuns)

    print("\n========== Additional information ==========")
    print("Program finished in %s seconds" % (time.time() - start_time))
    print("Simulations:", numberOfRuns)