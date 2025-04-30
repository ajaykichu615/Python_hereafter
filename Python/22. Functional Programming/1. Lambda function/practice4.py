# Create a function to check if first word of a string is of length 5 or not. If yes return True else False

length_of5 = lambda a:len(a.split()[0]) == 5
print(length_of5('Helloo World'))