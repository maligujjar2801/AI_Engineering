import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.end = time.perf_counter()
        print(f"Execution time : { self.end - self.start:.4f}")
        return True

with Timer() as timer :
 total = sum(range(100_000_000))