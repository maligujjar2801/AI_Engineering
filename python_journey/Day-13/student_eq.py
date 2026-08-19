class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.student_id == other.student_id


student_a = Student("Alice", 1001)
student_b = Student("Alice", 1001)
student_c = Student("Bob", 1002)

print(student_a == student_b)
print(student_a == student_c)
print(student_a == "Alice")
