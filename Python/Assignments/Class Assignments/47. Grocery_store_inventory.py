"""Given a grocery inventory dictionary:
grocery_store = {
    "Apples": {"price": 30, "stock": 50},
    "Bananas": {"price": 10, "stock": 100},
    "Milk": {"price": 50, "stock": 20},
}

Exercises:
Print the price of Milk.
Add a new item "Bread" with price 40 and stock 30.
Reduce the stock of Bananas by 20 after a sale.
Increase the price of Apples by 5.
Remove "Milk" from the inventory.
"""

gs = {
    "Apples": {"price": 30, "stock": 50},
    "Bananas": {"price": 10, "stock": 100},
    "Milk": {"price": 50, "stock": 20},
}

print(f"Price of Milk is: {gs['Milk']['price']}")
gs.update({'Bread':{"price": 40, "stock": 30}})
gs['Bananas']['stock'] -= 20
gs['Apples']['price'] += 5
gs.pop('Milk')

print(gs)
