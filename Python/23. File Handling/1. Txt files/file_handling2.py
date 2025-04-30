with open('new1.txt', 'r') as obj1:
    lst = obj1.readlines()
res = [x.strip() for x in lst] # using strip to remove new line which is also a white space
print(res)

with open('new2.txt', 'w') as obj2:
    pal = list(filter(lambda x:x.lower().endswith('n'),res))
    for i in pal:
        obj2.write(i+'\n')


