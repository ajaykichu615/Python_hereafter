"""Given the string "Python is fun", perform the following:

1. Split the sentence into words.

2. Reverse each word.

3. Join them back into a sentence.

Expected Output:
"nohtyP si nuf"

"""

str1 = "Python is fun"

lst = str1.split()

str1 =" "
res = ""

for i in lst:
    res += str1 + i[::-1]

print(res)
