#  Convert a list of temperatures in Celsius to Fahrenheit. Formula: F = (C × 9/5) + 32
#  lst=[56,78,98,34,12]

lst=[56,78,98,34,12]
temp_convert = list(map(lambda i: (i * 9/5) + 32, lst))
print(temp_convert)