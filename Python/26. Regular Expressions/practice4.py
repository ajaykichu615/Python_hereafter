# What are the complete addresses?
# Sample Result: ['173 Main St., Springfield RI 55924']

import re
with open(r'regular_expression.txt', 'r') as obj1:
    text = obj1.read()
pattern = re.compile(r'\d+\s[A-Za-z\s.]+,\s[A-Za-z\s]+\s[A-Z]{2}\s\d{5}')
print(pattern.findall(text))