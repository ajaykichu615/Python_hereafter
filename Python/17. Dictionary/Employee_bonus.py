# You have a dictionary of employees. Each has a salary and a years_of_service.
#
# Task:
#
# If an employee has worked for more than 5 years, give a 5000 bonus.
#
# Otherwise, keep the salary the same.
#
# Print employee name and final salary.



employees = {
    'John': {'salary': 40000,'years_of_service':6},
    'Sara': {'salary': 50000,'years_of_service':3},
    'Mike': {'salary': 45000,'years_of_service':8}
}

for employee, payment in employees.items():
    if payment['years_of_service'] > 5:
        payment['salary'] += 5000

for employee, payment in employees.items():
    print(f"{employee}: {payment['salary']}")

