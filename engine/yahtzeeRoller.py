import random

NUM_STANDARD_DICE = 5

def __mostFrequent(List):
    maxElement = max(set(List), key = List.count)
    numElement = List.count(maxElement)
    return numElement, maxElement

# Roll a dice once
def __individualRoll():
    return random.randrange(1,6)
    
# Roll 5 dice once each
def standardRoll(numDice = NUM_STANDARD_DICE):
    values = []

    for i in range(numDice):
        values.append(__individualRoll())

    return values

# This is weighted since we will save the best
# dice from the previous roll and reroll the rest
def weightedRoll(previousRoll):
    countMostFrequentOccurence, mostFrequentDiceElement = __mostFrequent(previousRoll)
    savedDice = [mostFrequentDiceElement] * countMostFrequentOccurence

    # Roll remaining dice that are not the majority
    roll = standardRoll(NUM_STANDARD_DICE-countMostFrequentOccurence)
    combination = savedDice + roll
    
    return combination 

if __name__ == "__main__":
    print("Cannot run this file as a stand alone script.")