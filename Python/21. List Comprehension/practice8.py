"""Generate a list of tuples with numbers and their squares
Example Data:
numbers = [1, 2, 3, 4, 5]
Expected Output:
[(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]"""

numbers = [1, 2, 3, 4, 5]
tup = [(i, i*i) for i in numbers]
print(tup)