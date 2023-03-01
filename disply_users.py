from main import Student

students = Students.select()
for student in students:
    print(student.stud_name, student.stud_)
