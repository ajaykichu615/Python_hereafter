# What ZIP codes appear in the text?
# Sample Result: ['55924']

import re
with open(r'regular_expression.txt', 'r') as obj1:
    text = obj1.read()
pattern = re.compile(r'\d{5}')
print(pattern.findall(text))