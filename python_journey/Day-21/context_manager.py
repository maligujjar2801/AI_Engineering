class MyContext:
    def __enter__(self):
        print("Entering Context...")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Leaving Context...")
        

with MyContext() as context:
    print("Working..")
