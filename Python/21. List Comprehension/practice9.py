"""Convert a dictionary into a formatted list of strings
Example Data:
num_dict = {1: "one", 2:"two", 3: "three"}
Expected Output:
["1-one", "2-two","3-three"]"""

num_dict = {1: "one", 2:"two", 3: "three"}
lst = [f"{i}-{j}" for i, j in num_dict.items()]
print(lst)