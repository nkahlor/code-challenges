import time


def time_it(func):
    def inner_handler(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took\n\t{time.perf_counter() - start:.5f}s")
        return result

    return inner_handler