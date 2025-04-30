# Combine first names and last names into full names.
# first = ['John', 'Jane'], last = ['Doe','Smith']

first = ['John', 'Jane']
last = ['Doe','Smith']

full_name = list(map(lambda f, l: f + ' ' + l, first, last))
print(full_name)