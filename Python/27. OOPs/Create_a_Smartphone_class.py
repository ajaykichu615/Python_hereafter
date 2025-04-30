# Create a Smartphone class
# Class variables: category, connectivity, OS (e.g., "Gadget", "5G", "Android")
# Object variables: brand, model, price
# Initialize object variables using the constructor.

class Smartphone:
    category = 'Gadget'
    connectivity = '5G'
    OS = 'Android'

    def __init__(self,b,m,p):
        self.brand = b
        self.model = m
        self.price = p

s1 = Smartphone("Samsung", "Galaxy S23", 74999)
s2 = Smartphone("OnePlus", "11R", 39999)
