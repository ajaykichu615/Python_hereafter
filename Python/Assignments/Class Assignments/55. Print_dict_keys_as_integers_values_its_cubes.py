num1 = input("Enter a number: ")  # Keep as string to iterate digits
dict1 = {}

for digit in num1:
    if digit.isdigit():  # Ensure it's a digit (skip signs/decimal points)
        dict1[digit] = int(digit) ** 3

print(dict1)