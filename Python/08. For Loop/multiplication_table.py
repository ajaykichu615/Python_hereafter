"""Write a program that allows the user to choose a number to get the multiplication table and then print
 first 10 multiplication tables of chosen number"""

num = int(input("Provide a number: "))
if num <= 0:
    print("Invalid number - no negatives allowed")
else:
    for i in range(1,11):
        print(f'{num}x{i} = {num*i}')
