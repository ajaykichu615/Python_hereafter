"""Generate a list of factorials for numbers 1 to 5
Example Data:
numbers = [1, 2, 3, 4, 5]
Expected Output:
[1, 2, 6, 24, 120]
"""

import math

numbers = [1, 2, 3, 4, 5]
factorials = [math.factorial(i) for i in numbers]
print(factorials)
