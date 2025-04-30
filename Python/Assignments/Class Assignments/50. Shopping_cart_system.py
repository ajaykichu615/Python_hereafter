"""A dictionary represents items added to a cart:

cart = {
    "Laptop": {"price": 50000, "quantity": 1},
    "Mouse": {"price": 700, "quantity": 2},
    "Keyboard": {"price": 1500, "quantity": 1},
}

Exercises:
Print the price of the Laptop.
Increase Mouse quantity by 1.
Remove "Keyboard" from the cart.
Add a new item "Headphones" with price 2000 and quantity 1.
Calculate the total cart value.
"""

cart = {
    "Laptop": {"price": 50000, "quantity": 1},
    "Mouse": {"price": 700, "quantity": 2},
    "Keyboard": {"price": 1500, "quantity": 1},
}

print(f"Price of Laptop: {cart['Laptop']['price']}")
cart['Mouse']['quantity'] += 1
cart.pop('Keyboard')
cart.update({'Headphones':{"price": 2000, "quantity": 1}})
total_value = sum(item["price"] * item["quantity"] for item in cart.values())
print(f"Total cart value: {total_value}")

