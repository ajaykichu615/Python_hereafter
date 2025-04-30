"""Extract odd-indexed characters from each word
Example Data:
words = ["apple", "banana", "cherry"]
Expected Output:
["pl", "aaa", "hry"] """

words = ["apple", "banana", "cherry"]
res = [i[1::2] for i in words]
print(res)