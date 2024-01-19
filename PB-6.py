from sys import maxsize
from itertools import permutations

V = 4


def travellingSalesmanProblem(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    next_permutation = permutations(vertex)
    min_route = None

    for i in next_permutation:
        current_pathweight = 0
        k = s
        route = [0]

        # noinspection PyTypeChecker
        for j in i:
            current_pathweight += graph[k][j]
            route.append(j)
            k = j

        current_pathweight += graph[k][s]
        route.append(s)

        if current_pathweight < min_path:
            min_path = current_pathweight
            min_route = route

    return min_path, min_route


# Driver Code
graph = [[-1, 10, 15, 20],
         [10, -1, 35, 25],
         [15, 35, -1, 30],
         [20, 25, 30, -1]]
s = 0
min_cost, route = travellingSalesmanProblem(graph, s)

print("Minimum Cost:", min_cost)
print("Route:", route)
