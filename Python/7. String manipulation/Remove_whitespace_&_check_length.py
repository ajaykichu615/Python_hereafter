"""Given the string "  Learn Python  ", remove leading and trailing spaces, and print its length before and after removing spaces.

Expected Output:

Original length: 16
Trimmed length:12"""

str1 = "  Learn Python  "
print(str1)
str2 = str.strip(str1)
print(f'Whitespace removed: {str2}')
len1 = len(str1)
len2 = len(str2)
print("Original length:", len1)
print("Trimmed length:", len2)
