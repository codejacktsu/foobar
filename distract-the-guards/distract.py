import time
# from fractions import gcd
from math import gcd

def timer(func):
    """decorator: prints process runtime"""
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter() - start_time
        print(f"Finished {func.__name__!r} in {end_time:.4f} secs")
        return result
    return wrapper


class Memoize:
    def __init__(self, function):
        self.cache = {}
        self.function = function

    def __call__(self, *args, **kwargs):
        key = str(args) + str(kwargs)
        if key in self.cache:
            print("memoized!")
            return self.cache[key]

        value = self.function(*args, **kwargs)
        print("key added: ", key, " ", value)
        self.cache[key] = value
        return value


@timer
def solution(n):
    if n < 2:
        return 1
    else:
        return solution(n-1) + solution(n-2)


def create_graph(lst):
    """ create graph of nodes connecting possible infinite loops
    :param lst: list of bananas
    :return g: generated graph"""

    g = {i: Node(i, value) for i, value in enumerate(lst)}
    for i in range(lst):
        for j in range(i, )
    return g


class Node:
    def __init__(self, i, value):
        self.pos = i
        self.value = value
        self.match = []
        self.weight = len(self.match)

    def find_match(self):



# class Graph:
#     def __init__(self, lst):
#         self.length = len(lst)


def infinite_check(pair):
    """ find whether pair results in infinite loop by checking power of 2
    :param pair: list of banana
    :return True/False: True for infinite loop, else False"""

    pair_sim = simple_form(pair)
    total = sum(pair_sim)
    return bool(total & (total - 1))


def simple_form(pair):
    """ reduce pair to simplest form
    :param pair: [a, b] pair
    :return pair: [a*, b*] simplified pair """

    d = gcd(pair[0], pair[1])
    pair[0] = pair[0] // d
    pair[1] = pair[1] // d
    return pair


# running
lst = [1, 7, 3, 21, 13, 19]
pair = [3, 4]
# print(solution(n))
# print(infinite_check(pair))
print(create_graph(lst)[1].weight)
