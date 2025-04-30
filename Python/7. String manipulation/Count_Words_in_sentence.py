"""Write a program that takes a user input sentence and:

1. Strips any leading and trailing spaces.


2. Splits the sentence into words.


3. Counts and prints the number of words.



Example Input:

"   Python makes coding fun and easy!   "

Expected Output: 6

"""

str1 = input("Provide an input sentence: ")
str2 = str.strip(str1)
str3 = str.split(str2)
length = len(str3)
print(f'The number of words in the above sentence is: {length}')