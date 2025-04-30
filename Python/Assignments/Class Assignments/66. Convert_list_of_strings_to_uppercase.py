"""Convert a list of strings to uppercase
Example Data:
words = ["hello", "world", "python", "list"]
Expected Output:
["HELLO", "WORLD", "PYTHON", "LIST"]
"""
words = ["hello", "world", "python", "list"]
res = [i.upper() for i in words]
print(res)
