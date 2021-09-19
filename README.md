# Yahtzee roller
Ever spent hours trying to roll a YAHTZEE and got curious - what if a robot could do this for me

## Introducing Yahtzee roller
A Yahtzee is a term borrowed from the game which specifies a five-of-a-kind dice roll. E.g. a dice roll with all sixes would be considered a Yahtzee. See: [Yahtzee](https://en.wikipedia.org/wiki/Yahtzee) for mroe information

This program has 3 different simulations to run

### Simulation 1: Number of Yahtzees
This will simulate a standard turn in the game of Yahtzee which is 3 rolls of the dice. On turn 2 and 3 you can save part of your previous turn and roll a subset of the 5 dice.

This simulation will give you how many Yahtzees you should expect to get if you complete a number of standard Yahtzee turns.

To run with the default simulation number:
```
python .\simulateNumYahtzees.py
```
OR provide a number of simulations you want
```
python .\simulateNumYahtzees.py 1000
```

Output 
```
========== Results ==========
Total number of Yahtzees: 89

========== Additional information ==========
Program finished in 0.009994983673095703 seconds
Simulations: 1000
```

### Simulation 2: Average rolls until Yahtzee
This simulation will give you the average rolls it takes to get a Yahtzee. This program will continue rolling the dice (saving some parts) until a five-of-a-kind is rolled.

```
python .\simulateAverageRollsUntilYahtzee.py 1000
```

Output
```
========== Results ==========
Median rolls until Yahtzee: 8.0
Average rolls until Yahtzee: 9.197
Minimum rolls until Yahtzee: 1
Maximum rolls until Yahtzee: 40

========== Additional information ==========
Program finished in 0.02500772476196289 seconds
Simulations: 1000
```

### Simulation 3: Standard turn score
This simulation will output the score of a standard 3 roll Yahtzee turn. A score of 4 represents four of a kind, 3 for three of a kind etc.

```
python .\simulateStandardTurnScore.py 1000
```

Output
```
Starting simulation...
========== Results ==========
Median score after 3 rolls: 3.0
Average score after 3 rolls: 3.341666666666667

========== Additional information ==========
Program finished in 0.011998414993286133 seconds
Simulations: 1000
```