"""Remove special characters from a list of words
Example Data:
words = ["he@llo!", "wo$rld", "py#thon!"]
Expected Output:
["hello", "world", "python"]
"""

words = ["he@llo!", "wo$rld", "py#thon!"]
res = [''.join (j for j in i if j.isalnum()) for i in words ]
print(res)