"""Write a program that counts the number of vowels (a, e, i, o, u) in a given sentence.

Example Input:

"Machine learning is amazing!"

Expected Output:

10"""
import re
str1 = input("Enter the sentence: ")
vowels = re.findall(r'[aeiouAEIOU]', str1)
print(len(vowels))

