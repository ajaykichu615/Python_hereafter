"""Flatten the list =
[[2,1,2],
[3,2,230],
[6,7,8],
[1,1,29]]"""


lst = [[2,1,2],
[3,2,230],
[6,7,8],
[1,1,29]]

new_lst = []
for i in lst:
    new_lst.extend(i)

print (new_lst)

