import random
import time
import statistics

NUM_STANDARD_DICE = 5
def mostFrequent(List):
    maxElement = max(set(List), key = List.count)
    numElement = List.count(maxElement)
    return numElement, maxElement

def individualRoll():
    return random.randrange(1,6)

def standardRoll(numDice = NUM_STANDARD_DICE):
    values = []

    for i in range(numDice):
        values.append(individualRoll())

    return values

def weightedTurn(previousRoll):
    # This is weighted since we will save the best
    # dice from the previous roll and reroll the rest

    countMostFrequent, mostFrequentElement = mostFrequent(previousRoll)
    savedDice = [mostFrequentElement] * countMostFrequent

    roll = standardRoll(NUM_STANDARD_DICE-countMostFrequent)
    combination = savedDice + roll
    
    return combination 

def standardTurn(): 
    turnOne = standardRoll(NUM_STANDARD_DICE)
    turnTwo = weightedTurn(turnOne)
    turnThree = weightedTurn(turnTwo)

    return turnThree

def countRollUntilYahtzee(): 
    turn = standardRoll(NUM_STANDARD_DICE)

    count = 1
    while (not isYahtzee(turn)):
        turn = weightedTurn(turn)
        count +=1 

    return count

# input is a standard roll e.g. [2,2,3,2,2]
def getAverageRollCount():
    final = standardTurn()

    countMostFrequent, mostFrequentElement = mostFrequent(final)

    return countMostFrequent

def attemptYahtzee():
    final = standardTurn()

    return isYahtzee(final)

def isYahtzee(roll):
    isYahtzee = roll.count(roll[0]) == len(roll)
    return isYahtzee

def numberOfYahtzeesSimulation(runs):
    yahtzees = 0
    for i in range(runs):
        isYahtzee = attemptYahtzee()

        if (isYahtzee):
            yahtzees+=1
    print("========== results ==========")
    print("runs:", runs)
    print("number of yahtzees:", yahtzees)

def averageRollsUntilYahtzeeSimulation(runs):
    numRollsToYahtzeeList = []
    totalSum = 0
    for i in range(runs):
        count = countRollUntilYahtzee()
        numRollsToYahtzeeList.append(count)
        totalSum += count
    print("Median:", statistics.median(numRollsToYahtzeeList))
    print("Average:", totalSum/runs)
    print("Minimum:", min(numRollsToYahtzeeList))
    print("Maximum:", max(numRollsToYahtzeeList))

def averageRoleTotalSimulation(runs):
    total_list = []
    total = 0
    for i in range(runs):
        score = getAverageRollCount()
        total_list.append(score)
        total += score

    print("Median:", statistics.median(total_list))
    print("Average:", total/runs)

start_time = time.time()
print("Starting simulation...")
# numberOfYahtzeesSimulation(1000000)
# averageRoleTotalSimulation(1000000)
averageRollsUntilYahtzeeSimulation(1000000)
print("program finished in %s seconds" % (time.time() - start_time))