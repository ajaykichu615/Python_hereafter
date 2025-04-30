# r+ - read, write
# w+ - write, read
# a+ - append, read

# Write 1-1000 to a text file line by line

# with open('new1.txt', 'r+') as obj1:
#     data = obj1.readline()
#     print(obj1.tell())
#     obj1.write('Poda')


with open('new2.txt', 'a+') as obj1:
    obj1.write('a')

