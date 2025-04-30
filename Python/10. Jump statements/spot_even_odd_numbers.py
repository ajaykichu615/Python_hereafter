"""Check if the list contains at least an odd number. If yes, the print and break iteration by
printing the 'list contains odd numbers also'
if all even, then print 'list contains only even numbers"""


lst = [12,28,34,56,78,11]

for i in lst:
    if i % 2 != 0:
        print("list contains odd numbers also")
        print(i)
        break

else:
    print("list contains only even numbers")
