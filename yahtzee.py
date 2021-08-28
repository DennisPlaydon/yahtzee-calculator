import random
import time

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

def attemptYahtzee():
    final = standardTurn()

    isYahtzee = final.count(final[0]) == len(final)
    return isYahtzee

def runSimulation(runs):
    yahtzees = 0
    for i in range(runs):
        isYahtzee = attemptYahtzee()

        if (isYahtzee):
            yahtzees+=1
    print("========== results ==========")
    print("runs:", runs)
    print("number of yahtzees:", yahtzees)

start_time = time.time()
runSimulation(1000000)
print("program finished in %s seconds" % (time.time() - start_time))