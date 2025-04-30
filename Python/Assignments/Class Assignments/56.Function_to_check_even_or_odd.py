"""Write a function to check even or odd that:
- Takes a number as parameter
- If even, print "Even" else :"Odd"""

def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = even_or_odd(68)
print(result)