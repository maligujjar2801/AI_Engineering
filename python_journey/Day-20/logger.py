from functools import wraps


def logger(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print(f"Starting... ")

        result = function(*args, **kwargs)

        print(f"Ended!")

        return result

    return wrapper


@logger 
def function():
    print("Working")

function()