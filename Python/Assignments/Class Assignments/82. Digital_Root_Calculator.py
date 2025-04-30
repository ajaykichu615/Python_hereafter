"""Digital Root Calculator
Q: Keep summing the digits of a number until one digit is left.
Input: 9875 → 9+8+7+5 = 29 → 2+9 =
11 → 1+1 = 2
Output:2"""

def digital_root_calculator(num):
    digits = num.split()
    count = len(num)
    while count <= len(num):
        num = sum(digits)

    return num

num1 = input('Enter the number: ')
print(digital_root_calculator(num1))