"""Extract common elements from two lists
Example Data:
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
Expected Output:
[4,5,6]"""

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
res = [i for i in list1 if i in list2]
print(res)


