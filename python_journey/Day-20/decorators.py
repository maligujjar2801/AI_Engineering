from functools import wraps

def retry(times):
    def decorater(function):

        @wraps(function)
        def wrapper(*args,**kwrgs):
            n = int(times)
            for i in range(n):
                try:
                    return function(*args,**kwrgs)
                    
                except Exception :
                    print(f"Attempt {i+1} Failed.")
            print("All attemts failed")

        return wrapper
    return decorater

@retry(4)
def divide(a,b):
    
    raise ValueError("Something went wrong...")
    print(a/b)
divide(10,2)
