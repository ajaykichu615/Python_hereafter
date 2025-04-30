str1 = """OrderID: 1001 | Date: 2024-11-01 | Customer: Alice Johnson | Item: Laptop | Quantity: 2 | Price: $1200  
OrderID: 1002 | Date: 2024-11-01 | Customer: Bob Smith | Item: Mouse | Quantity: 5 | Price: $25  
OrderID: 1003 | Date: 2024-11-02 | Customer: Alice Johnson | Item: Keyboard | Quantity: 1 | Price: $45  
OrderID: 1004 | Date: 2024-11-02 | Customer: Charlie Davis | Item: Monitor | Quantity: 3 | Price: $300  
OrderID: 1005 | Date: 2024-11-03 | Customer: Eva Green | Item: Laptop | Quantity: 1 | Price: $1200  
OrderID: 1006 | Date: 2024-11-03 | Customer: Bob Smith | Item: Mouse | Quantity: 10 | Price: $25  
OrderID: 1007 | Date: 2024-11-04 | Customer: David Kim | Item: Webcam | Quantity: 2 | Price: $75  
OrderID: 1008 | Date: 2024-11-04 | Customer: Alice Johnson | Item: Laptop | Quantity: 1|Price:$1200"""

# 1. Extract all the Order IDs.
# Sample Result: ['1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008']

# 2. Find all unique customer names.
# Sample Result: ['Alice Johnson', 'Bob Smith', 'Charlie Davis', 'Eva Green', 'David Kim']

# 3. Extract all dates from the orders.
# Sample Result: ['2024-11-01', '2024-11-01', '2024-11-02', '2024-11-02', '2024-11-03', '2024-11-03', '2024-11-04', '2024-11-04']

# 4. Get a list of all items sold.
# Sample Result: ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop', 'Mouse', 'Webcam', 'Laptop']

# 5. Extract all quantities ordered.
# Sample Result: ['2', '5', '1', '3', '1', '10', '2', '1']

# 6. Extract all the prices (just the numeric part).
# Sample Result: ['1200', '25', '45', '300', '1200', '25', '75', '1200']

# 7. Get all orders that include the item "Laptop".
# Sample Result: Full lines that include "Item:Laptop"

import re

orderid = re.compile(r"\d{4}")
unique_names = re.compile(r"[a-zA-Z]+\s[a-zA-Z]+")
dates = re.compile(r"\d+-\d+-\d+")
items = re.compile(r"Item:\s*([^|]+)")
quantities = re.compile(r"Quantity:\s*(\d+)")
prices = re.compile(r"Price:\s*\$\s*(\d+)")
laptop = re.compile(r'^.*Item:\s*Laptop.*$', re.MULTILINE)

matches1 = re.findall(orderid, str1)
matches2 = re.findall(unique_names, str1)
matches3 = re.findall(dates, str1)
matches4 = re.findall(items, str1)
matches5 = re.findall(quantities, str1)
matches6 = re.findall(prices, str1)
matches7 = re.findall(laptop, str1)

print(matches1)
print(list(set(matches2)))
print(matches3)
print(matches4)
print(matches5)
print(matches6)
print(matches7)