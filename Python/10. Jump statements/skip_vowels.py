"""Iterate through a string and skip vowels using continue."""

str1 = input("Enter a string: ")

for i in str1:
    if i in "aeiouAEIOU":
        continue
    print(i, end="")