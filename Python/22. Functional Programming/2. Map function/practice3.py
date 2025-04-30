# Extract last names from full names = ['John Doe', 'Jane Smith','Jim Beam']

names = ['John Doe', 'Jane Smith','Jim Beam']
last_name = list(map(lambda i: i.split()[1], names))
print(last_name)