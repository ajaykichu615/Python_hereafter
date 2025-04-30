"""Filter palindromes
words=['madam','hello','noon','python','civic']
"""

words=['madam','hello','noon','python','civic', 'Malayalam']
res = list(filter(lambda s:s.lower() == s[::-1].lower(), words))
print(res)