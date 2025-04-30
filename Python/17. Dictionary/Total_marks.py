# Question:
# You are given a dictionary where each key is a student's name.
# The value for each student is another dictionary with:
# Marks for three subjects: math, science, and english
# A grace key which is a boolean (True or False)
# Your task:
#
# If grace is True, add 50 to the total marks.
#
# If grace is False, just print the total marks as it is.
#
# Print the final total for each student.
#
# Expected behavior:
# For each student, print something like:
#
# Alice: 303
# Bob: 207
# Charlie: 323
# David:173

students = {
    "Alice": {"math": 90, "science": 80, "english": 83, "grace": True},
    "Bob": {"math": 70, "science": 67, "english": 70, "grace": False},
    "Charlie": {"math": 95, "science": 90, "english": 88, "grace": True},
    "David": {"math": 60, "science": 55, "english": 58, "grace": False}
}

result = {}
for student, details in students.items():
    total_marks = details["math"] + details["science"] + details["english"]
    if details["grace"]:
        total_marks += 50
    result[student] = total_marks

print(result)



