""" Find the first number divisible by 7 and 5 between 1 and 100 using break """
a = 0
b = 0
for i in range (1,101):
    if i % 7 == 0:
        a = i
    if i % 5 == 0:
        b = i
    if a != 0 and b != 0:
        break
print (f"First numbers to be divisible by 7 and 5 are {a} and {b} respectively")