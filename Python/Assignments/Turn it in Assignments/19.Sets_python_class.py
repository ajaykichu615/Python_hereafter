""""In a class of students learning multiple programming languages, students currently enrolled in Python are:

python_students = {"Akhil", "Sonia", "Varun", "Megha"}

Tasks:
1. "Divya" and "Rahul" also join the Python class. Update the set.

2. "Megha" decides to shift to the Java class. Remove her.

3. "Tom" tries to unenroll but was never in Python. Ensure no error occurs.

4. Display the final enrolled"""

python_students = {"Akhil", "Sonia", "Varun", "Megha"}

python_students.update({"Divya","Rahul"})
python_students.remove("Megha")
python_students.discard("Tom")

print(python_students)