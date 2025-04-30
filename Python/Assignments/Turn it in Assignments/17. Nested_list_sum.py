"""Given nested_list=[ [1,2,3], [4,5] , [6,7] ] find the sum of only first elements of each sublist.
(Output 1+4+6=11)"""

lst =[ [1,2,3], [4,5] , [6,7] ]

res = sum(item[0] for item in lst)

print(res)
