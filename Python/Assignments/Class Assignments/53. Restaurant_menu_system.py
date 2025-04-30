"""A dictionary represents restaurant menu items with their prices:
menu = {
    "Burger": 120,
    "Pizza": 250,
    "Pasta": 180,
}
Exercises:
Print the price of "Pizza".
Add "Fries" with a price of 80.
Increase "Pasta"'s price by 20.
Remove "Burger" from the menu.
Print all items in alphabetical order."""

menu = {
    "Burger": 120,
    "Pizza": 250,
    "Pasta": 180,
}

print(menu['Pizza'])
menu['Fries'] = 80
menu['Pasta'] += 20
menu.pop('Burger')
print(menu)
print(sorted(menu))