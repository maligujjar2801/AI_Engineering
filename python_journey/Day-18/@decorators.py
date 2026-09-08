def logger(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result
    return wrapper

@logger
def greet(name):
    print(f"Hello, {name}!")

greet("Ali")
