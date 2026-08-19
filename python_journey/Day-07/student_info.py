class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
student_1 = Student("Ali",17,'A')
student_2 = Student("Zainab",17,"A")
print("First Student :")
print("Name :\t",student_1.name)
print("Age :\t",student_1.age)
print("Grade :\t",student_1.grade)
print("Second Student :")
print("Name :\t",student_2.name)
print("Age :\t",student_2.age)
print("Grade :\t",student_2.grade)
