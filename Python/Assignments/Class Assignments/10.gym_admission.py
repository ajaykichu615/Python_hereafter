age = int(input("Enter your age: "))
member_type= input("Enter your member type (0 for Regular, 1 for Premium): ")
if member_type in [0,1]:
    if age < 18:
        if member_type == 1:
            print("Gym Fee is: 800 ")
        else:
            print("Gym Fee is: 500 ")
    elif 18 <= age <= 40:
        print("Gym Fee is: 1000 ")
    elif age > 40:
        if member_type == 1:
            print("Gym Fee is: 1200 ")
        else:
            print("Gym Fee is: 800 ")
else:
    print("Invalid input")