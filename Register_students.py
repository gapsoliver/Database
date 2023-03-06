from main import Student

try:
    student_name = input("Enter name \n")
    student_email = input("Enter email \n")
    student_password = input("Enter pasword \n")

    Student.create(stude_name=student_name, stude_email=student_email, stude_password=student_password)
except:
    print("Student created successfully")



