# Simple Calculator
    # addition---->0
    # Subtraction---->1
    # Multiplication---->2
    # Division---->3
    # Power---->4
    # Floor division---->5
    # Reminder---->6
    # Square root---->7
'''
print("************Welcome to the Simple Calculator!**************")
task = int(input("\nEnter the task number: "))
if task in range(0,8):
        if task == 0:
            print("Addition")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(num1 + num2)
        elif task == 1:
            print("Subtraction")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(num1 - num2)
        elif task == 2:
            print("Multiplication")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(num1 * num2)
        elif task == 3:
            print("Division")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(num1 / num2)
        elif task == 4:
            print("Power")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(num1 ** num2)
        elif task == 5:
            print("Floor division")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(num1 // num2)
        elif task == 6:
            print("Reminder")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(num1 % num2)
        elif task == 7:
            print("Square root")
            num = float(input("Enter the number: "))
            print(num ** 0.5)
else:
    print("Invalid task number")
'''

print("************Welcome to the Simple Calculator!**************\naddition---->0\nSubtraction---->1\nMultiplication---->2\nDivision---->3\nPower---->4\nFloor division---->5\nReminder---->6\nSquare root---->7")
task = int(input("\nEnter the task number: "))
x = float(input("Enter a number:"))
if task in range(8):
    if task == 7:
        print(f'Result:{x ** 0.5}')
    elif task == 6:

        y = float(input("Enter a second number: "))
        if y == 0:
            print("Error: Division by zero")
        else:
            print(f'Result:{x % y}')
    elif task == 5:
        y = float(input("Enter a second number: "))
        if y == 0:
            print("Error: Division by zero")
        else:
            print(f'Result:{x // y}')
    elif task == 4:
        y = float(input("Enter a second number: "))
        print(f'Result:{x ** y}')
    elif task == 3:
        y = float(input("Enter a second number: "))
        if y == 0:
            print("Error: Division by zero")
        else:
            print(f'Result:{x / y}')
    elif task == 2:
        y = float(input("Enter a second number: "))
        print(f'Result:{x * y}')
    elif task == 1:
        y = float(input("Enter a second number: "))
        print(f'Result:{x - y}')
    elif task == 0:
        y = float(input("Enter a second number: "))
        print(f'Result:{x + y}')
else:
    print("Invalid task")
