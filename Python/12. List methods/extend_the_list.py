"""Create a new list of even numbers and extend the original list with these numbers using the extend() method.
"""

from reverse_the_order import lst

list_new = []
list_new.extend([i for i in lst if i % 2 == 0])  # Adds multiple values at once

#print(list_new)




