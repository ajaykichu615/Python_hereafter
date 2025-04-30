"""Remove all occurrences of the number 10 from the list using a loop and remove()"""

lst = [25, 10, 345,224,10,32,20,10]
while 10 in lst:
    lst.remove(10)

print(lst)