import time


def time_it(func):
    def inner_handler(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        print(time.perf_counter() - start)

    return inner_handler