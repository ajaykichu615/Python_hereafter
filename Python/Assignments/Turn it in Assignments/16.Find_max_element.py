"""Find the largest number from the nested_list=[ [10, 20] ,[30,5], [15,40] ]"""

lst = [ [10, 20] ,[30,5], [15,40] ]

res = max(max(i) for i in lst)
print(res)