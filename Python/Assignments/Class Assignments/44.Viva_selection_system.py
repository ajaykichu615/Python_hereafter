""""Scenario:
A teacher is conducting a viva session for a group of students. The system should randomly pick a student from a set of students
and wait for the teacher’s confirmation before selecting the next student. After each viva, the teacher will enter the marks,
and the student's name along with their mark should be stored as an ordered pair (tuple) in a list.

Requirements:
1. Initialize a set of students who need to attend the viva.
2. Randomly pick a student from the set for viva.
3. After completing the viva for a student:
The teacher enters the marks for the student.
Store the student’s name and mark as a tuple inside a list.
Remove the student from the set, ensuring no repetition.
4. Ask the teacher whether to proceed to the next student or exit.
5. Repeat until all students have completed their viva.
6. At the end, display the final marks list in the order of viva completion.
---
Constraints:
The viva should only continue if there are students left in the set.
The teacher should have the option to stop the viva session anytime.
The system should ensure a student is not selected more than once.
Marks should be stored as an integer value.

Edge Cases to Consider:
What if the teacher enters an invalid input?
What if the teacher exits before all students complete the viva?
What if there’s only one student in the set?
"""

names = {"Alice", "Bob", "Charlie", "David", "Eve"}
names_copy = names.copy()
print("*************Viva Selection System***************\n\nHere's the list of students:", names)
viva_results = []

for i in range(len(names)):
    stud = names_copy.pop()
    print(f'Current viva student is {stud}')
    mark = int(input(f'Enter the mark of {stud}: '))
    while mark not in range(0,11):
        mark = int(input('Enter a valid mark: '))
    viva_results.append((stud,mark))

    res = input('Do you want to take viva for next student. \n If you want to stop, then type "stop" or else enter any key to continue:')
    if res.lower().strip() == "stop":
        exit()
    else:
        continue

print(viva_results)







