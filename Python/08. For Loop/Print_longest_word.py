"""Given string "Artificial Intelligence and Data Science"
1. Split the string
2. Find and print longest word"""

str1 = "Artificial Intelligence and Data Science"
lst = str1.split()
var1 = lst[0]
for i in lst:
    if len(i) > len(var1):
        var1 = i
print(f'Longest word is: {var1}')

