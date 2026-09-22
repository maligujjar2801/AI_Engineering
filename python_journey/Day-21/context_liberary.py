from contextlib import contextmanager


@contextmanager
def my_context():
    print("Entering")
    try:
        yield
    finally:

        print("Exiting")

with my_context() :
    print("Working")