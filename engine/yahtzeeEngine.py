import random
from engine import yahtzeeRoller

NUM_STANDARD_DICE = 5

def mostFrequent(List):
    maxElement = max(set(List), key = List.count)
    numElement = List.count(maxElement)
    return numElement, maxElement

def standardTurn(): 
    turnOne = yahtzeeRoller.standardRoll(NUM_STANDARD_DICE)
    turnTwo = yahtzeeRoller.weightedRoll(turnOne)
    turnThree = yahtzeeRoller.weightedRoll(turnTwo)

    return turnThree

def countRollUntilYahtzee(): 
    turn = yahtzeeRoller.standardRoll(NUM_STANDARD_DICE)

    count = 1
    while (not isYahtzee(turn)):
        turn = yahtzeeRoller.weightedRoll(turn)
        count +=1 

    return count

def isYahtzee(roll):
    isYahtzee = roll.count(roll[0]) == len(roll)
    return isYahtzee

if __name__ == "__main__":
    print("Cannot run this file as a stand alone script.")