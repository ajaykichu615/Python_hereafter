# Create a dictionary where the key is the customer name
# and the value is the total amount to be paid (Quantity × Price for each item they bought).
# You would:
# Extract all lines.
# Use regex to extract Customer, Quantity, and Price.
# Multiply quantity and price, and accumulate total per customer.
# Sample Result
# {
#   'Alice Johnson': 2*1200 + 1*45 + 1*1200,  # 2400 + 45 + 1200 = 3645
#   'Bob Smith': 5*25 + 10*25,               # 125 + 250 = 375
#   'Charlie Davis': 3*300,                  # 900
#   'Eva Green': 1*1200,                     # 1200
#   'David Kim': 2*75                        #150
# }

import re

data = """
Customer: Alice Johnson, Item: Laptop, Quantity: 2, Price: 1200
Customer: Alice Johnson, Item: Mouse, Quantity: 1, Price: 45
Customer: Alice Johnson, Item: Laptop, Quantity: 1, Price: 1200
Customer: Bob Smith, Item: Pen, Quantity: 5, Price: 25
Customer: Bob Smith, Item: Pencil, Quantity: 10, Price: 25
Customer: Charlie Davis, Item: Chair, Quantity: 3, Price: 300
Customer: Eva Green, Item: Laptop, Quantity: 1, Price: 1200
Customer: David Kim, Item: Notebook, Quantity: 2, Price: 75
"""

pattern = re.compile(r"Customer: ([A-Za-z ]+), Item: ([A-Za-z ]+), Quantity: (\d+), Price: (\d+)")

matches = pattern.findall(data)
print(matches)
