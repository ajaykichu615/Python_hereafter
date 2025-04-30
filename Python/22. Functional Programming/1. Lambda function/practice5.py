# Create a lambda function to check if a given string is palindrome or not

pal = lambda x: x.lower() == x[::-1].lower()
print(pal('Malayalam'))  # True
