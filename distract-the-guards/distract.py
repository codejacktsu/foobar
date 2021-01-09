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
def solution(n):
    if n < 2:
        return 1
    else:
        return solution(n-1) + solution(n-2)


# running
n = 10
print(solution(n))
