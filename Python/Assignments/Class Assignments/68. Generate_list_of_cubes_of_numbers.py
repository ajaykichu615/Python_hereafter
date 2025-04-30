"""Generate a list of cubes of numbers from 1 to 10
Example Data:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected Output:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
"""
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = [i**3 for i in num]
print(res)
