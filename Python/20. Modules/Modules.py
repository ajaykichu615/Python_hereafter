import random # random module

lst = ['ajay', 'jim', 'blake']
res = random.choice(lst) # choice is a function inside the random module
print(res)
random.shuffle(lst)
print(lst) # shuffle is a function for list

# random.choice()
# random.randint()
# random.shuffle()