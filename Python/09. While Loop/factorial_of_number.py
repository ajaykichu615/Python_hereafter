num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined")
else:
    result = 1
    i = num
    while i > 1:
        result *= i
        i -= 1

    print (f'Factorial of {num} is {result}')