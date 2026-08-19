try:
    with open("new.txt","r") as file :
        print(file.read())

except FileNotFoundError :
    print("File doesn't exist !")