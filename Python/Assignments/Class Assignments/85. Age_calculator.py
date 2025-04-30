from datetime import datetime
from calendar import monthrange

def calculate_detailed_age(dateofbirth):
    now = datetime.now()
    years = now.year - dateofbirth.year
    months = now.month - dateofbirth.month
    days = now.day - dateofbirth.day
    hours = now.hour - dateofbirth.hour
    minutes = now.minute - dateofbirth.minute
    seconds = now.second - dateofbirth.second

    if seconds < 0:
        seconds += 60
        minutes -= 1
    if minutes < 0:
        minutes += 60
        hours -= 1
    if hours < 0:
        hours += 24
        days -= 1
    if days < 0:
        prev_month = now.month - 1 if now.month > 1 else 12
        prev_year = now.year if now.month > 1 else now.year - 1
        days += monthrange(prev_year, prev_month)[1]
        months -= 1
    if months < 0:
        months += 12
        years -= 1

    return years, months, days, hours, minutes, seconds


input_date = input('Enter DOB (dd-mm-yyyy): ')
dob = datetime.strptime(input_date, "%d-%m-%Y")
age = calculate_detailed_age(dob)
print(f"Age: {age[0]} years, {age[1]} months, {age[2]} days, {age[3]} hours, {age[4]} minutes, {age[5]} seconds")
