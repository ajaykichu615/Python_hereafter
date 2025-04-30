"""WAP to input a number and find its factorial using while loop"""

num = int(input("Enter a number: "))
f = 1

if num < 0:
    print("Factorial is undefined")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range (1,num+1):
        f = f*i
    print(f"Factorial of {num} is : {f}")

