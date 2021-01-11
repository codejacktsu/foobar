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


def create_graph(lst):
    """ create graph of nodes connecting to all infinite loops inducing nodes
    :param lst: list of bananas
    :return g: generated graph"""

    g = {i: Node(i, value) for i, value in enumerate(lst)}
    for i in range(len(lst)-1):
        for j in range(i + 1, len(lst)):
            if infinite_check([g[i].value, g[j].value]):
                g[i].connect(j)
                g[j].connect(i)

    for i in range(len(lst)):
        for j in g[i].match:
            g[i].weight += g[j].length

    g['order'] = sorted(g.keys(), key=lambda x: g[x].weight)

    for i in range(len(lst)):
        g[i].sortbyweight(g['order'])

    return g


class Node:
    def __init__(self, i, value):
        self.pos = i
        self.value = value
        self.match = []
        self.length = 0
        self.weight = 0

    def connect(self, j):
        """ connect matching nodes
        :param j: position of matching node"""

        self.match.append(j)
        self.length = len(self.match)

    def sortbyweight(self, order):
        self.match.sort(key=lambda i: order.index(i)) # Python 3/2


def matching(g):
    """ match nodes starting with lowest weight to highest """

    guard = 0
    while g['order']:
        dq = g['order'].pop(0)
        temp_guard = 1
        if g[dq].weight:
            for i in g[dq].match:
                if i in g['order']:
                    g['order'].remove(i)
                    temp_guard = 0
                    break
        guard += temp_guard
    return guard


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

@timer
def solution(lst):
    g = create_graph(lst)
    return matching(g)


# running
lst = [1, 7, 3, 21, 13, 19]
# lst = [1, 1]
print(solution(lst))