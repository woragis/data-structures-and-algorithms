# used exclusevily for graphs without cycle

# do DFS
def dfs(at, V, visitedNodes, graph):
    V[at] = True
    # edges = graph.getEdgesOutFromNode(at)
    edges = graph[at]
    for edge in edges:
        if V[edge] == False:
            dfs(edge, V, visitedNodes, graph)


def topologicalSort(graph):
    # N = graph.numberofnodes()
    N = len(graph)
    V_visited = [False] * N
    ordering = [0] * N
    i = N-1  # index for ordering array

    for at in range(0, N):
        if V_visited[at] == False:
            visitedNodes = []
            dfs(at, V_visited, visitedNodes, graph)
            for nodeId in visitedNodes:
                ordering[i] = nodeId
                i -= 1
    return ordering
