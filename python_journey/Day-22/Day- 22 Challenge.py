students = [
    {"name": "Ali", "marks": 85},
    {"name": "Ahmed", "marks": 48},
    {"name": "Usman", "marks": 92},
    {"name": "Hamza", "marks": 55},
    {"name": "Bilal", "marks": 76}
]

names = [name for student in students for txt,name in student.items() if txt == "name"]

passed = [student for student in students for txt,marks in student.items() if txt == "marks" if marks >= 50]

print(names)

print("Passed Students :\n",passed)

name_marks ={ student["name"]:student["marks"] for student in students  }

print("Name and Marks",name_marks)

topped = {student:marks for student,marks in name_marks.items() if marks >= 80  }

print("A+ students :",topped)