"""Iterate the list and stop iteration if the list of number contains a negative number.
Also print that negative number when iteration stops"""

lst = [1,2,-4214,2,23,2,10]


for i in lst:
    if i < 0:
        print(f"Negative number {i}")
        break
    print(i)

else:
    print("List contains only positive numbers")