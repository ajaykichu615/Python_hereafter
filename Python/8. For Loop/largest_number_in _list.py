"""Find the largest number in a list without using max()
# lst=[1,10,21,30,34,42,45]"""

lst=[1,10,21,30,34,42,45]
largest = lst[0]
for i in lst[1:]:
    if i > largest:
        largest = i

print("Largest number is :", largest)


