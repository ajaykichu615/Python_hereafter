# What phone numbers are listed?
# Sample Result: ['615-555-7164']

import re
with open(r'regular_expression.txt', 'r') as obj1:
    text = obj1.read()
pattern = r'\d{3}-\d{3}-\d{4}'
matches = re.findall(pattern,text)
print(matches)