"""Calculate the sum of all even numbers in the list.
#lst=[1,10,21,30,34,42,45]"""

lst=[1,10,21,30,34,42,45]
res = 0
for i in lst:
    if i % 2 == 0:
       res += i
print(f' The sum of even numbers in the list is: {res}')