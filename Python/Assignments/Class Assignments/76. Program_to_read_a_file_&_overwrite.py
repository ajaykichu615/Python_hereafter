# Write a program to read from a file and then overwrite the first 5 characters with "HELLO".

with open ('myfile.txt', 'w+') as f:
    f.write('Hello')

