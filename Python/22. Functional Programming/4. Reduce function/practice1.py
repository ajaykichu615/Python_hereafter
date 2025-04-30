# combine list of strings into one single list

from functools import reduce
lst = ['apple','orange','grapes']
res = [reduce(lambda x,y: x+y, lst)]
print(res)