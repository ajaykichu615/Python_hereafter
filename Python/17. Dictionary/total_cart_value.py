# Calculate total cart value:
# cart={"Pen":{'price':20,'quantity':5},
#       "Laptop":{'price':40000,'quantity':2},
#       "PS2":{'price':100000,'quantity':1},
#       "Headset":{'price':799,'quantity':3}}

cart={"Pen":{'price':20,'quantity':5},
        "Laptop":{'price':40000,'quantity':2},
        "PS2":{'price':100000,'quantity':1},
        "Headset":{'price':799,'quantity':3}}
print(cart.values())
total_price = sum(item['price']*item['quantity'] for item in cart.values())
print(total_price)
