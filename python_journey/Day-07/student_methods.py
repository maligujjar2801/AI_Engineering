class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    subjects ={
           "Math": 40,
           "Science": 46,
           "Computr Science": 50
        }
    def add_subject(self, subject, marks):
        self.subjects.update({subject:marks})
    def show_marks(self):
        for subject, marks in self.subjects.items():
            print(f"{subject}: {marks}")
student_1 = Student("Ali",17)
print(f"Name: {student_1.name}")
print(f"Age: {student_1.age}")
print("Marks:")
student_1.show_marks()
add_subject = input("Enter subject name to add: ")
add_marks = int(input("Enter marks for the subject: "))
print("After adding new subject:")
student_1.add_subject(add_subject, add_marks)
student_1.show_marks()