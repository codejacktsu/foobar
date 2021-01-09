import time


def timer(func):
    """decorator: prints process runtime"""
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter() - start_time
        print(f"Finished {func.__name__!r} in {end_time:.4f} secs")
        return result
    return wrapper


@timer
def printer(msg):
    return print(msg)


# running
msg = "test"
printer(msg)
