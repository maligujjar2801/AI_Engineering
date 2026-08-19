exit = False 
students = ["Ali","Zainab","Fatima"]
while not exit :
    print("""
      ===== Student List =====

    1. View Students
    2. Add Student
    3. Remove Student
    4. Search Student
    5. Exit""")
    n=int(input("Enter number (1-5) :"))
    if n== 1 :
        print(students)
    elif n == 2 :
        add_student = input("Enter the name     of student :")
        if not add_student :
            print("Enter a name first !!!")
        else:
            students.append(add_student)
      
    elif n==3 :
        remove_student =input("Enter                the name of student.")
        if not remove_student :
            print("Enter the name first !!!")
        else:
            students.remove(remove_student)
            print("Student removed succesfully.")
    
    elif n== 4:
        search_student =input("Enter the name of student :")
        if search_student in students :
            print("The student is in the list .")
        else :
            print("The student is not in the list .")
            print("Type 2 to add student.")
    elif n== 5 :
        exit = True 
    
     
        
    
        