from functools import wraps
import time
def timer(function):
    @wraps(function)
    def wrapper(*args,**kwrgs):
        start = time.perf_counter()
        function(*args,**kwrgs)
        end = time.perf_counter()
        print(f"Execution Completed✅\nTime Taken : {end - start :.4f} seconds")

    return wrapper

@timer
def calculate():
    total = 0

    for number in range(1_000_000):
        total += number

    return total


calculate()