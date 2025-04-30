num1 = int(input("Enter the number: "))
factorial = 1

if num1 < 0:
    print("Factorial not defined for negative numbers")
elif num1 == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num1+1):
        factorial *= i
    print(f'Factorial of {num1} is : {factorial}')
