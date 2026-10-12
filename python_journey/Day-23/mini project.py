students = {
    101 : {"name" : "Ali" , "marks" : 92},
    102 : {"name" : "Zainab" , "marks" : 89},  
    103 : {"name" : "Fatima" , "marks" : 95}
}

id = int(input("Enter the id of student:"))
student = students.get(id)

if student:
    print(f"Name: {student["name"]}\nMarks : {student["marks"]}")