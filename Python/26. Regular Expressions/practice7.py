# What are the domains of the email addresses?
# Sample Result: ['bogusemail.com']

import re
with open(r'regular_expression.txt', 'r') as obj1:
    text = obj1.read()
pattern = r"@([\w.-]+\.\w+)"
domains = re.findall(pattern, text)

unique_pattern = set(domains)
print(list(unique_pattern))