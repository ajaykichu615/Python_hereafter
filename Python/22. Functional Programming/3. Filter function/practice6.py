"""Filter students who passed.
# Given a list of students score dictionaries, filter students who scored>=50.
students = [
    {"name": "Alice", "score": 45},
    {"name": "Bob", "score": 75},
    {"name": "Charlie", "score": 60}
"""
students = [
    {"name": "Alice", "score": 45},
    {"name": "Bob", "score": 75},
    {"name": "Charlie", "score": 60}]

res = list(filter(lambda student: student['score']>=50, students))
print(res)
