"""Write a Python program that takes two lowercase strings, "hello" and "world", concatenates them with a space in between, and capitalizes the first letter of each word.

Expected Output:

"Hello World"
"""

str1 = input("Enter the first string:")
str2 = input("Enter the second string:")
if str1.islower() and str2.islower():
    str3 = str1 + " " + str2
    print(f'Concatenated string is {str3}')
else:
    print("Invalid input. Only lower case characters accepted")