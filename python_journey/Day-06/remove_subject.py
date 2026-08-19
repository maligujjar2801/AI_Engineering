subjec;ats=["math","science","computer","urdu","english"]
remove_sub= input("Enter the name of subject :")
sub=remove_sub.lower()
if sub in subjects :
    subjects.remove(sub)
    print("The subject is removed from the list.")
else :
    print("The subject is not in the list.")