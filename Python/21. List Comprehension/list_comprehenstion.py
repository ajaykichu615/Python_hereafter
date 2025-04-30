# Syntax : [expression for iterating variable in iterable object if condition]

"""lst = [i for i in range(1,101) if i % 3 == 0 and i % 7 == 0 and i < 100]
print(lst)"""

lst = ['Python', 'program', 'apple', 'data', 'science']

res = [len(i) for i in lst]
print(res)
