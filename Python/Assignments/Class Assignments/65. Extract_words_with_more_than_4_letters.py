""" Extract words with more than 4 letters
Example Data:
words = ["cat", "elephant", "dog", "giraffe", "tiger"]
Expected Output:
["elephant", "giraffe", "tiger"]
"""
words = ["cat", "elephant", "dog", "giraffe", "tiger"]
res = [i for i in words if (len(i)>4)]
print(res)
