"""Implement factorial(n) that returns the factorial of a number using recursion."""

n = int(input("Enter a number: "))
def factorial(num):
    if num < 0:
        return "Factorial not defined for negative numbers"
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(n))

