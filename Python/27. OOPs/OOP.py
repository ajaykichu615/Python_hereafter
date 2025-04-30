# Object-Oriented Programming using class

class Student:
    institute = 'Luminar'    # Class Variables: institute, course & course_duration
    course = 'Data Science'
    course_duration = 7

    def __init__(self,name,age):
        self.student_name=name  # Object Variables: student_name & student_age
        self.student_age=age

stud1 = Student('Ajay', 27)  # Objects: stud1 & stud2
stud2 = Student('Roshan', 28)
print(stud1.student_name)
print(stud2.student_age)
print(Student.course)