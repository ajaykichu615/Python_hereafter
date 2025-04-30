"""Extract words that contain at least one digit
Example Data:
words = ["abc", "h3llo", "w0rld", "python", "c0d1ng"]
Expected Output:
["h3llo", "w0rld", "c0d1ng"]
"""

words = ["abc", "h3llo", "w0rld", "python", "c0d1ng"]
res = [i for i in words if any(j.isdigit() for j in i) ]
print(res)
