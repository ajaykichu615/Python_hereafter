lst = ['apple', 'banana', 'grapes', 'kiwi', 'jackfruit', 'pineapple']
res = list(filter(lambda x: x[0].lower()=='a', lst))
print(res)