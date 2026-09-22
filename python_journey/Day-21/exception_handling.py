class MyContext:
    def __enter__(self):
        print("Entering Context...")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(exc_type)
        print(exc_value)
        print(traceback)
        print("Leaving Context...")
        return True

with MyContext() as context:
    print(10/0)
