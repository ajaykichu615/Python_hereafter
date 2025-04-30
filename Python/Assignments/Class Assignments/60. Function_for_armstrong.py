"""Write is_armstrong(n) to check if a number is an Armstrong number (e.g., 153 = 1³ + 5³ + 3³)."""

def is_armstrong(num):  # Removed the "1usage" typo
    num_str = str(num)
    n = len(num_str)
    total = 0
    for i in num_str:
        digit = int(i)
        total += digit ** n
    return 'Number is Armstrong' if total == num else "Not an Armstrong number"

number = int(input("Enter the number: "))  # Added space after colon for readability
print(is_armstrong(number))