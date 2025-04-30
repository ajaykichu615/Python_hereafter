# Write 1-1000 numbers to text file in each line.

with open('numbers.txt', 'w') as obj1:
    for i in range(1, 1001):  # Generates numbers from 1 to 1000
        obj1.write(str(i) + '\n')  # Writes each number as a string to the file
