"""Write a program that calculates the electricity bill based on the following slab rates (per unit).
Units consumed cost per unit;
upto 100 units cost 5 per unit
101 to 200 units cost 7 per unit
201 to 300 units cost 10 per unit
above 300 units cost 15 per unit"""

unit = int(input("Enter the number of units consumed: "))
bill = None
if unit <= 100:
    bill = unit * 5
elif 101 <= unit <= 200:
    bill = (100 * 5) + (unit - 100) * 7
elif 201 <= unit <= 300:
    bill = (100 * 5) + (200 * 7) + (unit - 200) * 10
elif unit > 300:
    bill = 100 * 5 + 200 * 7 + 150 * 10 + (unit - 300) * 15
else:
    print("Invalid unit")
print(f'The electricity bill is {bill}rs')