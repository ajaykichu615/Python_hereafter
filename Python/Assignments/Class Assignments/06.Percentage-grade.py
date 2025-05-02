percentage = float(input("Enter your percentage: "))
if percentage > 90:
    print("Grade A")
elif 80 < percentage <= 90:
    print("Grade B")
elif 60 <= percentage <= 80:
    print("Grade C")
else:
    print("Grade D")
