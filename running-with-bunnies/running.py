from util import timer, Memoize


#brute force

def solution(times, time_limit):
    graph = [bellman_ford(times, layer) for layer, _ in enumerate(times)]
    flag = neg_cycle_check(graph, times, time_limit)

    if len(times) <= 2:
        return []
    elif flag:
        return list(range(len(times)-2))

    return graph, flag

def bellman_ford(cost, origin):
    """ Use Bellman-Ford algorithm to find shortest path
    check for negative cycle"""

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


def neg_cycle_check(graph, times, time_limit):
    """ check for negative cycle """

    n = len(graph)
    for i in range(n):
        for j in range(n):
            for z in range(n):
                if graph[i][z] > graph[i][j] + times[j][z] and graph[0][j] < time_limit:
                    return True
    return False


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
