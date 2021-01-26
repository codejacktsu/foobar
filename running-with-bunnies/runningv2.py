from util import timer, Memoize


def solution(times, time_limit):
   pass


class Vertex:
    def __init__(self, idx):
        self.idx = idx
        self.bunnies = []


def solver(graph):
    for z in range(len(graph)-1):
        for start, total_cost in enumerate(graph):
            if total_cost == 'inf':
                continue
            for end in range(len(graph)):
                delta = cost[start][end]
                if graph[end] == 'inf':
                    graph[end] = delta
                else:
                    graph[end] = min(graph[end], graph[start] + delta)




# times = [[0, 1, 1, 1, 1],
#          [1, 0, 1, 1, 1],
#          [1, 1, 0, 1, 1],
#          [1, 1, 1, 0, 1],
#          [1, 1, 1, 1, 0]]
# time_limit = 3

times = [[0, 2, 2, 2, -1],
         [9, 0, 2, 2, -1],
         [9, 3, 0, 2, -1],
         [9, 3, 2, 0, -1],
         [9, 3, 2, 2, 0]]
time_limit = 1

print(solution(times, time_limit))
