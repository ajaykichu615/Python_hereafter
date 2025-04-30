num = int(input("Enter a number: "))
sum1 = 0
temp = abs(num)

while temp > 0:
    sum1 += temp % 10
    temp //= 10
print (f"Sum of digits: {sum1}")

