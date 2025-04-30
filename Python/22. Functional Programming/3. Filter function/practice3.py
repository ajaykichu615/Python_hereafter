# Filer non-empty strings from the list.
#remove empty strings from the list

strings = ['hello','','world','python']
res = list(filter(lambda s:s != '',strings))
print(res)
