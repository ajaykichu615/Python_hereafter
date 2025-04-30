"""Prime Number Checker

Create is_prime(n) that returns True if n is a prime number, otherwise False."""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # check odd factors up to square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

x = int(input("Enter the number to be checked: "))
print(is_prime(x))

