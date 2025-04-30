"""Flatten a nested list.
Convert [ [1,2] ,[3, 4], [5] ] into [1,2,3,4,5]"""

lst1 =[ [1,2] ,[3, 4], [5] ]
res = []

for i in lst1:
    res.extend(i)

print(res)