# Extract year from date strings dates = ['01/01/2020', '15/08/1947','31/12/1999']

dates = ['01/01/2020', '15/08/1947','31/12/1999']
res = list(map(lambda s: s.split('/')[-1], dates))
print(res)