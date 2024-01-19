graph = {
    "a": ["b", "c"],
    "b": [ "d"],
    "c": ["e"],
    "d": [],
    "e": []
}
visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for next_node in graph[s]:
            if next_node not in visited:
                visited.append(next_node)
                queue.append(next_node)

print("Following is the BFS:")
bfs(visited, graph, 'a')