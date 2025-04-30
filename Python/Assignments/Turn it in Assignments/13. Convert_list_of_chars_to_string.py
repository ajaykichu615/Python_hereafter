"""1.Convert a list of characters to a string
[ 'h', 'e' ,'l', 'l' ,'o']  to  "hello"
"""

lst1 = [ 'h', 'e' ,'l', 'l' ,'o']
res = ""

for char in lst1:
    res += char

print(res)