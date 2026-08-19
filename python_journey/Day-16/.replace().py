with open("aligi.txt","r") as file :
    content = file.read()
    content = content.replace("Gujjar","Gorsi")
    file.seek(0)
    print(content)