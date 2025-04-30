"""Write a function count_vowels(s) that returns the number of vowels in a given string. Allow the user to
input a string and display the vowel count"""

s = input("Enter a string: ") #Global variable declared
def count_vowels(c=0):
    vowels = "aeiou"
    for char in s:
        if char.lower() in vowels:
            c += 1
    return c

print("Number of vowels:",count_vowels())
