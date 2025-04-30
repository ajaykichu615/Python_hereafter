years = float(input("Enter the years of service: "))
if years > 5:
    salary = float(input("Enter the salary: "))
    if salary < 50000:
        bonus = float(salary * 0.10)
    else:
        bonus = float(salary * 0.05)
    print("The bonus of the employee is:", bonus)
else:
    print("Not eligible for bonus")