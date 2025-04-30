"""Filter prime numbers.
# Write a helper function to check for prime numbers and use filter() to return only prime numbers.
numbers=[2,3,4,5,6,7,8,9,10]
"""

def helper_function_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):  # check only odd numbers
        if n % i == 0:
            return False
    return True

numbers=[2,3,4,5,6,7,8,9,10]
res = list(filter(helper_function_prime, numbers))
print(res)