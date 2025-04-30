import argparse
import math
import sys

# Parser without "choices"
parser = argparse.ArgumentParser()
parser.add_argument("--type", help="Type of payment: 'annuity' or 'diff'")
parser.add_argument("--payment", type=float, help="Monthly payment amount")
parser.add_argument("--principal", type=float, help="Loan principal")
parser.add_argument("--periods", type=int, help="Number of periods (months)")
parser.add_argument("--interest", type=float, help="Annual interest rate (as a percentage)")
args = parser.parse_args()

# Manual validation
args_list = [args.payment, args.principal, args.periods, args.interest]

if args.type not in ["annuity", "diff"]:
    print("Incorrect parameters")
    sys.exit()

if args.interest is None:
    print("Incorrect parameters")
    sys.exit()

if any(arg is not None and arg < 0 for arg in args_list):
    print("Incorrect parameters")
    sys.exit()

i = args.interest / (12 * 100)  # monthly interest rate

if args.type == "diff":
    if args.principal is None or args.periods is None or args.payment is not None:
        print("Incorrect parameters")
        sys.exit()

    total_payment = 0
    for month in range(1, args.periods + 1):
        d = math.ceil(
            (args.principal / args.periods) + i * (args.principal - (args.principal * (month - 1)) / args.periods))
        total_payment += d
        print(f"Month {month}: payment is {d}")

    overpayment = int(total_payment - args.principal)
    print(f"\nOverpayment = {overpayment}")

elif args.type == "annuity":
    if args.principal is not None and args.payment is not None and args.periods is None:
        n = math.ceil(math.log(args.payment / (args.payment - i * args.principal), 1 + i))
        years = n // 12
        months = n % 12
        if years == 0:
            print(f"It will take {months} months to repay this loan!")
        elif months == 0:
            print(f"It will take {years} years to repay this loan!")
        else:
            print(f"It will take {years} years and {months} months to repay this loan!")
        overpayment = int((args.payment * n) - args.principal)
        print(f"Overpayment = {overpayment}")

    elif args.principal is not None and args.periods is not None and args.payment is None:
        payment = math.ceil(args.principal * (i * (1 + i) ** args.periods) / ((1 + i) ** args.periods - 1))
        print(f"Your monthly payment = {payment}!")
        overpayment = int((payment * args.periods) - args.principal)
        print(f"Overpayment = {overpayment}")

    elif args.payment is not None and args.periods is not None and args.principal is None:
        principal = args.payment / ((i * (1 + i) ** args.periods) / ((1 + i) ** args.periods - 1))
        print(f"Your loan principal = {int(principal)}!")
        overpayment = int((args.payment * args.periods) - principal)
        print(f"Overpayment = {overpayment}")

    else:
        print("Incorrect parameters")

