"""If a user purchases items worth:
• ₹5000 or more → 20% discount • ₹2000 - ₹4999
 → 10% discount • Less than ₹2000 → No discount
Calculate and display the final price."""

print ('********DISCOUNT CALCULATOR********')

purchase_amt = float(input("Enter the purchase amount: "))

if purchase_amt >= 5000:
    discount = 0.20
    print (f'Final Amount: {purchase_amt * discount}')
elif 2000 <= purchase_amt <= 4999:
    discount = 0.10
    print (f'Final Amount:{purchase_amt * discount}')
else:
    discount = 0
    print(f' Final Amount:{purchase_amt}')
    print("No discount applied")

