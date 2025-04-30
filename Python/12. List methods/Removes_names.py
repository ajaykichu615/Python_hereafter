"""Given a list of names, remove names starting with 'A'."""


lst = input("Enter the names seperated by space: ").split()

for name in lst:
    if name.startswith('A'):
        lst.remove(name)
print(lst)