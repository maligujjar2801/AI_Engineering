with open('aligi.txt','w+') as file :
    file.write("Ali")
    file.seek(0)
    print(file.read())
    