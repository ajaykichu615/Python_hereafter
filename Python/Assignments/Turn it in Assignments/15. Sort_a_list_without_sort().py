"""Write a program that sorts a list in descending order without using sort() or sorted()"""


# Bubble sort
lst = [2,3,45,67,8,75,3,42,49]
n = len(lst)

for i in range(n):
    for j in range(n-i-1):
        if lst[j] < lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)





