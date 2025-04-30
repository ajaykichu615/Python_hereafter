# Take an input number from the user (say5) and write its multiplication table(1 to 10) to table.txt.

with open('table.txt', 'w') as obj1:
    num = int(input("Enter a number: "))
    for i in range(num + 1):
        obj1.write(f'{num} x {i} = {num * i}\n')



