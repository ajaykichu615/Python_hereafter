# 1. Extract all patient names.
# Sample Result: ['John Doe', 'Alice Brown', 'Michael Lee', ...]
#
# 2. List all doctors who had appointments.
#
# 3. Extract appointments that were scheduled with Dr. Smith.
#
# 4. Extract all appointments scheduled on or after 2025-04-03.
#
# 5. Get all appointments from the Cardiology department.
#
# 6. List all appointment times before 12:00 noon.
#
# 7. Extract all unique departments patients visited.
#
# 8. Find all appointments where Fee is greater than $100.
#
# 9. Create a dictionary where:
#
# Key = Patient Name
# Value = Total Fee Paid
# Sample Output:
# {
#   'John Doe': 500,
#   'Alice Brown': 200,
#   'Michael Lee': 300,
#   'Sara Kim': 300,
#   'Tom White': 80
# }
#
# 10. Count how many times each doctor had appointments.
# Tip: Research about time, date related modules.

import re

with open(r'medical_appointments-1.txt','r') as obj1:
    text = obj1.read()

names = re.findall(r'Name: (\w*\s?\w*)', text)
doctors = re.findall(r'Doctor: (\w+\.\s?\w+)', text)
Dr_Smith = re.findall(r'^.*Doctor: Dr\. Smith.*$', text, re.MULTILINE)
appointments = re.findall(r'^.*Date: 2025-04-0[3-9].*$|^.*Date: 2025-04-[1-9][0-9].*$', text, re.MULTILINE)
cardiology = re.findall(r'^.*Department: Cardiology.*$', text, re.MULTILINE)
before_noon = re.findall(r'Time: (0[0-9]:[0-5][0-9]|11:[0-5][0-9])', text)
departments = re.findall(r'Department: (\w*)', text)
fee = re.findall(r'^.*Fee: \$(?:1[0-1][1-9]|1[2-9]\d|[2-9]\d{2,}).*$', text, re.MULTILINE)

print(names)
print(list(set(doctors)))
for appt in Dr_Smith:
    print(appt)
print(appointments)
print(cardiology)
print(before_noon)
print(list(set(departments)))
print(fee)
