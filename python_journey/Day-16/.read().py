import os

if not os.path.exists("aligi.txt"):
    # create the file so opening in 'r' won't fail
    open("aligi.txt", "w").close()

with open("aligi.txt", "r") as file:
    file.seek(0)
    print(file.read())
    file.seek(0)
    print(file.read(2))
    file.seek(0)
    print(file.readline(),end='')
    print(file.readline())
    file.seek(0)
    print(file.readlines())