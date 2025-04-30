num = int(input("Enter a number: "))
rev = 0
temp = abs(num)

while temp > 0:
    digit = temp % 10
    rev = (rev * 10) + digit
    temp //= 10

if num < 0:
    rev = -rev

print(f"Reversed number: {rev}")
