def print_solution(dist):
    print("Vertex \tDistance from Source")
    for node in range(len(dist)):
        print(node, "\t", dist[node])

def min_distance(dist, spt_set):
    min_dist = float('inf')
    min_index = -1
    for u in range(len(dist)):
        if dist[u] < min_dist and not spt_set[u]:
            min_dist = dist[u]
            min_index = u
    return min_index

def dijkstra(graph, src):
    vertices = len(graph)
    dist = [float('inf')] * vertices
    dist[src] = 0
    spt_set = [False] * vertices

    for _ in range(vertices):
        x = min_distance(dist, spt_set)
        spt_set[x] = True

        for y in range(vertices):
            if graph[x][y] > 0 and not spt_set[y] and dist[y] > dist[x] + graph[x][y]:
                dist[y] = dist[x] + graph[x][y]

    print_solution(dist)

# Small and simple graph for testing
graph = [
    [0, 4, 0, 0, 0],
    [4, 0, 8, 0, 0],
    [0, 8, 0, 7, 0],
    [0, 0, 7, 0, 9],
    [0, 0, 0, 9, 0]
]

source_vertex = 0
dijkstra(graph, source_vertex)