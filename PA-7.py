graph = {
    "a": ["b", "c"],
    "b": [ "d"],
    "c": ["e"],
    "d": [],
    "e": []
}
visited = []

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.append(node)
        for next_node in graph[node]:
            dfs(visited, graph, next_node)

print("Following is the DFS:")
dfs(visited, graph, "a")

