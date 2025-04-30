""" Write a program to determine if a given number is Armstrong or not """

num1 = int(input("Provide a number: "))
num2 = str(num1)
digits = len(num2)
sum1 = 0
for i in num2:
    sum1 += int(i) ** digits
if sum1 == num1:
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")
