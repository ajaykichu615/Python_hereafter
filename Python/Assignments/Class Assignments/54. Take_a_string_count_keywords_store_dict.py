"""Write a program to take a sentence as input and find out a dictionary with each unique word as
 key. The count of occurrences of that word as the value."""

text = input("Enter the sentence: ").lower()
keywords = ['apple', 'banana', 'mango']
word_list = text.split()
keyword_count = {}


for key in keywords:
    keyword_count[key] = word_list.count(key)

print(keyword_count)

