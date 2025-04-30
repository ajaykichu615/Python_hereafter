"""Given a list of names, remove names starting with 'A'"""

lst = ['Ameer', 'Ambrose', 'Brandivila', 'Blake', 'Manu', 'Aalaap']

new_lst = [name for name in lst if not name.startswith(('A','a'))]

print(new_lst)





