def prime(n : int):
    if n < 2:
        return 'Not prime'
    for i in range(2,n//2+1):
        if n % i == 0:
            return 'Not prime'
    return 'prime'

print(prime(38))

