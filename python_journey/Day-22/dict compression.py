students = {
    "Ahmad" : 60,
    "ALi" : 90,
    "Hamza" : 86
}
print(f"Total Students :\n")

for student , marks in students.items():
    print(f"\t{student} : {marks}")

passed = {student : marks for student,marks in students.items() if marks > 80}

print("\nPassed Students :\n")
for student , marks in passed.items():
    print(f"\t{student} : {marks}")
