def kruskal_algorithm(graph):
    result = []  # to store the edges of the minimum spanning tree
    edges = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))

    edges.sort( key=lambda item: item[2])  # sort edges by weight
    parent = [i for i in range(len(graph))]

    def find(subset, i):
        if subset[i] != i:
            subset[i] = find(subset, subset[i])
        return subset[i]

    def union(subset, x, y):
        xroot = find(subset, x)
        yroot = find(subset, y)
        subset[xroot] = yroot

    e = 0  # index for result[]
    i = 0  # index for sorted edges

    while e < len(graph) - 1:
        u, v, w = edges[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e += 1
            result.append((u, v, w))
            union(parent, x, y)

    return result


# Example usage
graph_example = [
    [0, 19, 5, 0, 0],
    [19, 0, 5, 9, 2],
    [5, 5, 0, 1, 6],
    [0, 9, 1, 0, 1],
    [0, 2, 6, 1, 0]
]

minimum_spanning_tree = kruskal_algorithm(graph_example)

print("Edges in the Minimum Spanning Tree:")
for u, v, weight in minimum_spanning_tree:
    print(f"{u} - {v} : {weight}")


