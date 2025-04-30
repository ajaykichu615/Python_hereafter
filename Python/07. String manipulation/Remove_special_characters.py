"""Write a program that removes special characters (like !@#$%^&*()) from the given string.

Example Input:

"Hello@World! Python#Rocks?"

Expected Output:

"HelloWorld PythonRocks"""

import re
str1 = input("Enter the string: ")
str2 = re.sub(r'[^A-Za-z0-9 ]', '', str1)
print(str2)