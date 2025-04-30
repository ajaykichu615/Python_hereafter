""" Write a function roll_dice() that simulates rolling a six sided die and returns a random number
between 1 & 6."""


import random
def roll_dice():
    return random.randint(1,6)

print("Rolling the dice.....:", roll_dice())