# You are given a list of students with their marks.
# Group the students into a dictionary based on these rules:
#
# A Grade: 90 and above
# B Grade: 75–89
# C Grade: 50–74
# Fail: below 50
# Expected output (grouped dictionary):
#
# {
#     'A': ['Arun'],
#     'B': ['Bala', 'Eshan'],
#     'C': ['Chitra', 'Farah'],
#     'Fail':['Deepa']
# }


students = {
    'Arun': 92,
    'Bala': 76,
    'Chitra': 67,
    'Deepa': 45,
    'Eshan': 89,
    'Farah': 52
}

grouped = {'A': [], 'B': [], 'C': [], 'Fail': []}

for name, mark in students.items():
    if mark >= 90:
        grouped['A'].append(name)
    elif 75 <= mark <= 89:
        grouped['B'].append(name)
    elif 50 <= mark <= 74:
        grouped['C'].append(name)
    else:
        grouped['Fail'].append(name)

print(grouped)