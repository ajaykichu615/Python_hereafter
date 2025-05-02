age = int(input("Enter the age:"))
if age < 0:
    print("Please enter a valid age")
elif age < 18:
    print("You are not eligible to vote")
else:
    print("You can vote")
