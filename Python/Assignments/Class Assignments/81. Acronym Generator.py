"""Acronym Generator
Q: Input a phrase, output its acronym.
Input: "laugh out loud"
Output:"LOL"""

def acronym_gen(str1):
    acronym = ""
    for word in str1:
        acronym += word[0].upper()

    return acronym

phrase = input().split()
print(acronym_gen(phrase))