"""Given a nested_list=[ [1,2], [3,4,5] ,[6] ] creat a new list , storing the length of each inner list.
(Output[2,3,1])"""

lst = [[1, 2], [3, 4, 5], [6]]
new_lst = []

for i in lst:
    new_lst.append(len(i))

print(new_lst)
