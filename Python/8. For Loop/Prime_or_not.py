num = int(input("Enter the number: "))
c = 0
for i in range(2,num//2+1):
    if num % i == 0:
        c += 1
if c != 0 or num == 1:
    print("It's not a prime number")
else:
    print("It's a prime number")




