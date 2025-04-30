# Which email addresses are found?
# Sample Result: ['davemartin@bogusemail.com']

import re
with open(r'regular_expression.txt', 'r') as obj1:
    text = obj1.read()
pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
print(pattern.findall(text))
