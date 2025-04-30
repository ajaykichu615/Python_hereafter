"""Given the string "  Data Science is awesome!   ", perform the following:

1. Remove extra spaces from the beginning and end using strip().


2. Split the sentence into a list of words using split().



Expected Output:

"Data Science is awesome!"
['Data', 'Science', 'is', 'awesome!']
"""

str1 = "  Data Science is awesome!  "
str2 = str.strip(str1)
str3 = str.split(str1)
print(str1)
print(str2)
print(str3)