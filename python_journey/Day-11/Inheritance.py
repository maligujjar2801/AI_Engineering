class Person:
    def introduce(self):
        print("Hello, my name is Ali.")

class Student(Person):
    pass

student = Student()
student.introduce()  # Output: Hello, my name is Ali.