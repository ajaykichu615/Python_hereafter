"""Extract words that start with a vowel
Example Data:
words = ["apple", "banana", "orange", "grape", "elephant"]
Expected Output:
["apple", "orange", "elephant"]
"""

words = ["apple", "banana", "orange", "grape", "elephant"]
vowels = 'aeiou'
res = [i for i in words if i.startswith(tuple(vowels))]
print(res)