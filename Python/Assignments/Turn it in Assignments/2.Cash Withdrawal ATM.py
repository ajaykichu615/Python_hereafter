Withdrawal_Amt = int(input("Enter the amount to withdraw:"))
Current_Balance = 100000

if Withdrawal_Amt % 10 == 0:
    if Withdrawal_Amt <= Current_Balance:
        print("The transaction is successful")
    else:
        print("Insufficient Balance")
else:
    print("Invalid amount")
