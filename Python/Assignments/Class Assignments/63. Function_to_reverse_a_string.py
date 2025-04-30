""" Reverse a String
Write reverse_string(s) that takes a string and returns its reverse string."""

def reverse_string(s):
    lst = list(s)
    res = lst[::-1]
    return ''.join(res)

str1 = input("Enter the string: ")
print(reverse_string(str1))