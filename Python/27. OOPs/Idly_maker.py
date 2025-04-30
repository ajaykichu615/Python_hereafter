# Exercise: IdlyMaker Class
# Create a class called IdlyMaker to simulate an automatic idly making machine.
#
# Attributes:
# capacity: Maximum number of idlis the maker can make at once (e.g., 6 or 8).
# batter_level: Amount of batter available (in idli units).
# cooked_idlis: Number of idlis currently cooked and ready to serve (initially 0).
#
# Methods:
# 1. add_batter(amount)
# Adds batter to the machine (1 unit = 1 idli).
# Increases batter_level.

# 2. make_idlis(number)
# Cooks the given number of idlis, only if:
# There’s enough batter.
# The number is within the machine's capacity.
# Updates batter_level and cooked_idlis.
#
# 3. serve_idlis(number)
# Serves the requested number of idlis if available.
# Decreases cooked_idlis.
# If not enough idlis are ready, show how many are available.
#
# 4. status()
# Shows current batter level and number of cooked idlis available.

# Sample Usage:
#
# machine = IdlyMaker(capacity=6)
# machine.add_batter(10)
# machine.make_idlis(5)
# Output: 5 idlis cooked!
#
# machine.status()
# Output: Batter left: 5, Cooked idlis: 5
#
# machine.serve_idlis(3)
# Output: 3 idlis served!
#
# machine.status()
# Output: Batter left: 5, Cooked idlis:2

class IdlyMaker:
    def __init__(self,capacity):
        self.capacity = capacity
        self.batter_level = 0
        self.cooked_idly = 0

    def add_batter(self,amount):
        if amount>0:
            self.batter_level+=amount
            print('Batter added successfully')
        else:
            print('Enter a positive value')

    def make_idly(self,no_of_idly):
        if no_of_idly<=self.capacity:
            if no_of_idly<=self.batter_level:
                self.batter_level-=no_of_idly
                self.cooked_idly+=no_of_idly
                print(f'{no_of_idly} idly cooked')
            else:
                print('Insufficient batter')
        else:
            print(f'Cannot cook more than {self.capacity} idly at once')

    def serve_idlis(self,number):
        if number<=self.cooked_idly:
            print(f'{number} idlis served')
            self.cooked_idly-= number
        else:
            print(f'Sorry. Only {self.cooked_idly} idlis are available')

    def status(self):
        print(f'Batter level: {self.batter_level}\nCooked idly: {self.cooked_idly}')

machine = IdlyMaker(capacity=6)
machine.add_batter(10)
machine.make_idly(5)
machine.status()
machine.serve_idlis(3)
machine.status()
