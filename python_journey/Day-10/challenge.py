class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi , I'm {self.name}.")

class Student(Person):
    def __init__(self,grade):
        super().__init__("Ali")
        self.grade = grade
    def study(self):
        print("Studying...")

student = Student("A")
student.introduce()  # Output: Hi, I'm Ali.
student.study()      # Output: Studying...
      