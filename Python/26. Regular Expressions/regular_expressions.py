str1 = 'name: Ajay Gosh mail: ajy123@gmail.com phone: 8292929193 Course: Data Science'

import re

phone = re.compile(r'\d{10}') # \d means digits --- here it means 10 digits because \d is right next to {10} (exact occurrences)
print(phone.findall(str1))
new_val = re.compile(r'\D{21}') # \D means non-digits ---here its calling 11 occurrences of all non-digits.
print(new_val.findall(str1))
new_phone = re.compile(r'\b\D{20}\b') # \b means word boundary
print(new_phone.findall(str1))
mail = re.compile(r'\b\w+@gmail.com\b') # \w means alphanumeric--- '+' means one or more occurrence---'.' means everything except newline
print(mail.findall(str1))
course = re.compile(r'Course: ([a-z, A-Z]+)')
print(course.findall(str1))
