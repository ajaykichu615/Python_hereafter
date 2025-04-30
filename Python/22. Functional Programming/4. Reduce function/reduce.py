# syntax reduce(function, iterable)


# cumulative sum
lst = [2,3,4,5]

from functools import reduce

res = reduce(lambda x,y: x + y**2, lst, 0) # 0 acts as initial value
print(res)
