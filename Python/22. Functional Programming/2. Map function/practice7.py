# Convert floats to strings with prefix  ₹
# prices = [99.99, 149.50, 10.0]

prices = [99.99, 149.50, 10.0]
res = list(map(lambda p:str(p)+'₹', prices))
print(res)
