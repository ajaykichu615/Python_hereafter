"""Fibonacci Sequence Generator

Implement fibonacci(n) that returns the first n Fibonacci numbers as a list.
"""

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

x = int(input("How many fibonacci numbers: "))
print(fibonacci(x))