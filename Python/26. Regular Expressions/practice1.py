# What are the full names in the text?
# Sample Result: ['Dave Martin']


import re
with open(r'regular_expression.txt', 'r') as obj1:
    text = obj1.read()
    names = re.findall(r"^([A-Z][a-z]+(?: [A-Z][a-z]+)+)", text, re.MULTILINE)
    print(names)
