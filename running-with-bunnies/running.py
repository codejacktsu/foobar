from util import timer, Memoize


#brute force

def solution(times, time_limit):
    return [bellman_ford(times, layer) for layer, _ in enumerate(times)]

def bellman_ford(cost, origin):
    """ Use Bellman-Ford algorithm to find shortest path"""

    graph = []
    for i in range(len(cost)):
        if i == origin:
            graph.append(0)
        else:
            graph.append('inf')
    for z in range(len(graph)-1):
        beg_graph = graph.copy()
        for start, total_cost in enumerate(graph):
            if total_cost == 'inf':
                continue
            for end in range(len(graph)):
                delta = cost[start][end]
                if graph[end] == 'inf':
                    graph[end] = delta
                else:
                    graph[end] = min(graph[end], graph[start] + delta)
        if graph == beg_graph:
            break
    return graph


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
# print(bellman_ford(times, 0))