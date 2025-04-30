num = int(input("Enter a number: "))
i = 2 # start checking from 2
is_prime = True

while i * i <= num and num > 1:
    if num % i == 0:
        is_prime = False
        break
    i += 1

while num <= 1:
    is_prime = False
    break

print(f"{num} is a prime number." if is_prime else f"{num} is not a prime number.")

