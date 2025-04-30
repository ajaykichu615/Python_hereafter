""""A Data Science Course has students enrolled:

students = {"Anil", "Benny", "Chitra","Dev"}

Tasks:
1. Add "Esha" to the course.

2. Remove "Chitra" as she dropped out.

3. A new batch joins: {"Faisal", "Gina", "Hari"}. Add them to the set.

4. Try removing "Riya", who was mistakenly listed but never enrolled. Ensure no error occurs.

5. Print the updated student list.
"""

students = {"Anil", "Benny", "Chitra","Dev"}
students.add("Esha")
students.remove("Chitra")
students.update({"Faisal", "Gina", "Hari"})
students.discard("Riya")
print(students)