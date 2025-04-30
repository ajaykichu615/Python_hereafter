"""Extract numbers divisible by both 3 and 5
Example Data:
numbers = [10, 15, 30, 45, 60, 75, 80, 90, 100]
Expected Output:
[15, 30, 45, 60, 75, 90]"""

numbers = [10, 15, 30, 45, 60, 75, 80, 90, 100]
res = [i for i in numbers if i % 3 == 0 and i % 5 == 0]
print(res)