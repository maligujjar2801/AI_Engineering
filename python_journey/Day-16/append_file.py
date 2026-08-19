file = open("aligi.txt","a+")
print(file.read())
file.write("\nI'm  Ali Gujjar.")
file.seek(0)  # Seek to beginning to read the updated content
print(file.read())
file.close()
