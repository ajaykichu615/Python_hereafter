num = int(input("Enter a number: "))
ld = num % 10
if ld % 3 == 0:
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 3")