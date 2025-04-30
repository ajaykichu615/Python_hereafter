# Question: Create a Shopping eKart System
#
# Write a Python program to create a class named ShoppingCart that simulates a simple online shopping cart system.
#
# Attributes:
# customer_name: Name of the customer.
# cart: A dictionary to store items where the key is the item name and the value is a dictionary with:
# price: Price of the item
# quantity: Quantity added to the cart
#
# Methods:
#
# 1. add_item(item_name, price, quantity)
# Add an item to the cart with given price and quantity.
# If the item already exists, update its quantity by adding the new quantity.
#
# 2. remove_item(item_name)
# Remove an item completely from the cart if it exists.
# If the item does not exist, display an appropriate message.
#
# 3. update_item(item_name, quantity)
# Update the quantity of a particular item.
# If quantity is set to 0, remove the item from the cart.
# If the item does not exist, show an error message.
#
# 4. calculate_total()
# Calculate and return the total amount to be paid for all the items in the cart.
#
# 5. display_cart()
# Display all the items in the cart along with their quantity, price per unit, and total price for that item.
#
# 6. empty_cart()
# Remove all items from the cart (cart becomes empty).
#
# Sample Usage:
#
# cart = ShoppingCart("Alice")
# cart.add_item("Laptop", 60000, 1)
# cart.add_item("Mouse", 500, 2)
# cart.add_item("Keyboard", 1500, 1)
# cart.display_cart()
# # Should show: Laptop, Mouse, Keyboard with their quantities and prices
#
# cart.update_item("Mouse", 1)
# # Now Mouse quantity becomes 1
#
# cart.remove_item("Keyboard")
#
# cart.calculate_total()
# # Should return total amount = (60000 * 1) + (500 * 1)
#
# cart.empty_cart()
# cart.display_cart()
# # Should show the cart is empty
#
# Additional Points:
#
# Use a dictionary inside the cart for flexible management.
# Think about error handling when an item is not found.

class ShoppingCart:
    def __init__(self,customer_name,cart):
        self.customer_name=customer_name
        self.cart={}

    def add_item(self,item_name,price,quantity):
        if item_name in self.cart:
            self.cart[item_name]['quantity'] += quantity
        else:
            self.cart[item_name]={'price':price,'quantity':quantity}

    def remove_item(self,item_name):
        if item_name in self.cart:
            del self.cart[item_name]
            print(f"{item_name} removed from the cart.")
        else:
            print(f"{item_name} not found in the cart.")

    def update_item(self,item_name,quantity):
        if item_name in self.cart:
            if quantity == 0:
                del self.cart[item_name]
                print(f"{item_name} removed from the cart because quantity is 0.")
            else:
                self.cart[item_name][quantity] = quantity
                print(f"Quantity of {item_name} updated to {quantity}.")
        else:
            print(f"{item_name} does not exist in the cart.")

    def calculate_total(self):
        total=0
        for item in self.cart.values():
            total+=item['price']*item['quantity']
        print(f'Total amount payable is {total}')

    def display_cart(self):
        if not self.cart:
            print('Cart is empty')

        print("Items in the cart:")
        print("{:<15}{:<10}{:<10}{:<10}".format("item","Price","Quantity","Total"))
        print('-'*50)

        for item_name,item_info, in self.cart.items():
            price=item_info['price']
            quantity=item_info['quantity']
            total_price=price*quantity
            print("{:<15} {:<10} {:<10} {:<10}".format(item_name, price, quantity, total_price))

    def empty_cart(self):
        self.cart.clear()
        print('Cart is empty now')




cart = ShoppingCart("Alice",{})
cart.add_item("Laptop", 60000, 1)
cart.add_item("Mouse", 500, 2)
cart.add_item("Keyboard", 1500, 1)
cart.display_cart()
cart.update_item("Mouse", 1)
cart.remove_item("Keyboard")
cart.display_cart()
cart.calculate_total()
cart.empty_cart()


