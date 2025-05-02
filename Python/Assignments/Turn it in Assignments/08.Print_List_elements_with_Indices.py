"""Print List Elements with Their Indices
Given the list:
items = ["car", "bike", "bus"]
Write a for loop to print each item with its index.
Expected Output:

0:car
1:bike
2:bus"""

items = ["car", "bike", "bus"]
for i in range(len(items)):
    print(f'{i}:{items[i]}')