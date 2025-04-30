# Which state abbreviations are mentioned?
# Sample Result: ['RI']

import re
with open(r'regular_expression.txt', 'r') as obj1:
    text = obj1.read()
pattern = re.compile(r'\D[A-Z]{2}')
print(pattern.findall(text))