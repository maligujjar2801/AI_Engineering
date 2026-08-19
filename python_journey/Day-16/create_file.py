with open("new.txt","x+") as file:
    file.write("New file created !")
    file.seek(0)
    print(file.read())