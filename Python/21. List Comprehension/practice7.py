"""Reverse each word in a given list
Example Data:
words = ["apple", "banana", "cherry", "date"]
Expected Output:
['elppa', 'ananab', 'yrrehc', 'etad']"""

words = ["apple", "banana", "cherry", "date"]
rev_words = [i[::-1] for i in words]
print(rev_words)