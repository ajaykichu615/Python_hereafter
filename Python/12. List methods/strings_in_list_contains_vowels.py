"""Find out all strings in a list which contain at least a vowel. The result should be
stored in another list"""

lst = ['Python','fly', 'gym','langauge','digit','Try','why']
lst_new = []
vowels = 'aeiouAEIOU'

for string in lst:
    for char in string:
        if char in vowels:
            lst_new.append(string)
            break
print(lst_new)