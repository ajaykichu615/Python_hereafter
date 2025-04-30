"""B/w 1 - 100 , create two separate lists using iteration for even and odd numbers"""

lst1 = []
lst2 = []

for num in range(1,101):
    if num % 2 == 0:
        lst1.insert(len(lst1), num)
    else:
        lst2.insert(len(lst2), num)
print("Even list: ", lst1)
print("Odd list:", lst2)