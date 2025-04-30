"""Create a dictionary with students and their marks in three subjects:

students = {
    "Alice": {"Math": 85, "Science": 90, "English": 88},
    "Bob": {"Math": 78, "Science": 88, "English": 92},
    "Charlie": {"Math": 92, "Science": 80, "English": 85},
}
Exercises:
Print Alice’s Science marks.
Add a new student "David" with random marks.
Update Bob’s English marks to 95.
Remove "Charlie" from the dictionary.
Print all student names and their average marks.
"""

stud = {
    "Alice": {"Math": 85, "Science": 90, "English": 88},
    "Bob": {"Math": 78, "Science": 88, "English": 92},
    "Charlie": {"Math": 92, "Science": 80, "English": 85},
}
avg = 0

print("Alice's science marks:", stud['Alice']['Science'])
stud.update({'David':{"Math": 95, "Science": 80, "English":89}})
stud['Bob'].update({'English':95})
print(stud['Bob'])
stud.pop('Charlie')

for name, marks in stud.items():
    avg = sum(marks.values())/len(marks)
    print(f"{name}'s average marks: {avg:.2f}")