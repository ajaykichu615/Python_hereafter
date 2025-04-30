"""Convert a list of temperatures from Celsius to Fahrenheit using list comprehension °F = °C × (9/5) + 32."""

lst = ['35', '28', '33']
lst_new = [(int(i) * 9/5) + 3 for i in lst if i.isdigit() ]
print(lst_new)

