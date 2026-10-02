import os

def create_file(filename,content=""):
    try:
        with open(filename,"x") as file:
            file.write(content)
        print("File created succesfully !")
        return file
        
    except FileExistsError as ex:
        print("File already exists.")
        raise FileExistsError("File already exists.")
    
def read_file(filename,n=None):
    with open(filename,"r") as file:
        content = file.read(n)
        return f"Content :\n{content}"

def delete_file(filename):
    os.remove("ex.txt")
    print("File deleted succesfully!")

def get_path(filename):
    file_path =  os.path.abspath(filename)
    return file_path


file = create_file("ex.txt","My name is Muhammad Ali.\nI'm 17 years old.")
print(read_file("ex.txt",))
print("Path:  ",get_path("ex.txt"))
delete_file("ex.txt")

