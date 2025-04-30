"""Create a list of first and last characters of each word
Example Data:
words = ["apple", "banana", "cherry"]
Expected Output:
["ae", "ba", "cy"]"""

words = ["apple", "banana", "cherry"]
res = [i[0]+i[-1] for i in words]
print(res)

