# Remove spaces from strings
# sentences = ['hello world', 'python map', 'lambda function']

sentences = ['hello world', 'python map', 'lambda function']
res = list(map(lambda s:s.replace(' ', ''), sentences))
print(res)