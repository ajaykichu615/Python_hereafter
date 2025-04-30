# Write a Python program to create a class called ATMCardHolder that simulates basic ATM operations. The class should have the following:
#
# Attributes:
#
# name – cardholder's name
# pin – 4-digit PIN
# balance – Current account balance
#
# Methods:
#
# 1. display_details() – Display card holder’s name and balance.
# 2. withdraw(amount, entered_pin) – Withdraw the given amount after verifying the PIN. Ensure there are sufficient funds.
# 3. deposit(amount, entered_pin) – Deposit the given amount after verifying the PIN.
# 4. change_pin(old_pin, new_pin) – Allow the user to change their PIN after verifying the old one.
#
# Note: Every transaction (withdraw, deposit, and PIN change) should require correct PIN entry.
#
# Example Usage:
# card_holder = ATMCardHolder("John Doe", 4321, 10000)
# card_holder.display_details()
# card_holder.withdraw(2000, 4321)
# card_holder.deposit(500, 4321)
# card_holder.change_pin(4321,1234)

class ATMCardHolder:

    def __init__(self,name,pin):
        self.name=name
        while not (str(pin).isdigit() and len(str(pin)) == 4):
            pin = input('Invalid PIN.\nEnter a new PIN:')
        else:
            self.pin = str(pin)
        self.balance=1000

    def display_details(self):
        print(f"Name: {self.name}\nBalance: {self.balance}")

    def withdraw(self,amount,pin):
        if self.pin==str(pin):
            if amount <= self.balance:
                print(f'{amount}.Rs withdrawn successfully.')
                self.balance-=amount
            else:
                print('Insufficient balance')
        else:
            print('Incorrect PIN')

    def deposit(self,amount,pin):
        if self.pin==str(pin):
            if amount > 0:
                self.balance+=amount
                print(f'{amount}.Rs deposited successfully')
            else:
                print('Invalid amount')
        else:
            print('Incorrect PIN')

    def change_pin(self,old_pin,new_pin):
        if self.pin==str(old_pin):
            if str(new_pin).isdigit() and len(str(new_pin)) == 4:
                self.pin = new_pin
                print('PIN changed successfully')
            else:
                self.pin = input('Invalid PIN.\nEnter a new PIN:')
        else:
            print('Wrong pin. Try again!')







obj1 = ATMCardHolder('Abu','4552')
obj1.display_details()
obj1.withdraw(450,4552)
obj1.deposit(502,4552)
obj1.change_pin(4552,2255)
obj1.display_details()