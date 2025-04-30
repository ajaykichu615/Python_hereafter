"""Given the string "   Python programming is powerful   ", perform the following:

1. Remove unnecessary spaces using strip().


2. Split the string into words using split().


3. Print the first and last words separately.



Expected Output:

"Python"
"powerful"
"""

str1 = "  Python programming is powerful  "
str2 = str.strip(str1)
str3 = str.split(str1)
print(str3, '\n', str3[0], '\n', str3[-1])