# Write a program to accept a user's name and age, then write it to a file named user.txt. After
# writing, read the file and display the content



with open('person.txt','w') as obj1:
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    obj1.write(name + '\n')
    obj1.write(str(age) + '\n')

with open('person.txt', 'r') as obj1:
    content = obj1.read().splitlines()  # Reads all lines into a list
    print(content)
