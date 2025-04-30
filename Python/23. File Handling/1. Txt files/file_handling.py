# read
# write
# append

with open('new.txt', 'r') as obj1: # provide full file location if it's not in the same folder as py file.
    print(obj1.tell()) # to find the cursor /index position at any given point
    print(obj1.seek(23))  # to modify the position of cursor / index
    var1 = obj1.readline()
    print(var1)
    var2 = obj1.readline()
    print(var2)
    print(obj1.tell())


# Read mode methods:
    # obj.read()
    # obj.readline()
    # obj.tell()
    # obj.seek()
