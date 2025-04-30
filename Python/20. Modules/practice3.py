""" Write a function pick_winner(names) that selects a random winner from a list of names"""

import random
lst = ['Sam', 'David', 'Larry', 'Kesav']

def pick_winner(names):
    return random.choice(names)


print("Lucky Winner: ", pick_winner(lst))