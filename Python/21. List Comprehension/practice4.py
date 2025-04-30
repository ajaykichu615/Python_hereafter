"""Extract all vowels from the string "Hello, how are you?" using list comprehension."""

str1 = "Hello, how are you?"
lst = [i for i in str1 if i.lower() in 'aeiou']
print(lst)