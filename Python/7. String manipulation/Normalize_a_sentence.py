"""Question:
Given the string "   Hello, HOW are YOU?   ", perform the following:

1. Remove unnecessary spaces using strip().


2. Convert the sentence to lowercase.


3. Split the sentence into words using split().



Expected Output:

"hello, how are you?"
['hello,', 'how', 'are', 'you?']"""

str1 = "  Hello, How are you?  "
str2 = str.strip(str1)
str3 = str.lower(str2)
str4 = str.split(str2)

print(str2)
print(str4)