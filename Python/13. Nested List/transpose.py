"""Transpose list =
[[2,1,2],
[3,2,230],
[6,7,8],
[1,1,29]]"""


lst = [[2,1,2],
[3,2,230],
[6,7,8],
[1,1,29]]

transpose_lst = []

for i in range(len(lst[0])): #iterating number of columns
    new_row = [] #adding empty lists
    for row in lst: #
        new_row.append(row[i])
    transpose_lst.append(new_row)
print(transpose_lst)


