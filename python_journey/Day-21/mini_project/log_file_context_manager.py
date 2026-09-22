from pathlib import Path


class LogFile:

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "a")

        print("File opened")
        print("File location:", Path(self.filename).resolve())

        return self.file

    def __exit__(self, exc_type, exc, tb):
        self.file.close()

        print("File Closed")

        if exc_type:
            print("Exception:", exc)

        return True


with LogFile("log_file.log") as file:
    file.write("Application started\n")
    file.write("Processing data\n")
    raise ValueError("Something went wrong.")