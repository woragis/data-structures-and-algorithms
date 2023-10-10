# graphs
# nodes + edges
# node: values inside
# edge -> relationship to other nodes
# dfs: uses stack
# bfs: uses queue

def depthFirstSearch(graph, source):
    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        print(current, end=' ')
        for neighbor in graph[current]:
            stack.append(neighbor)


def depthFirstSearchRecursive(graph, source):
    print(source, end=' ')
    for neighboor in graph[source]:
        depthFirstSearchRecursive(graph, neighboor)


def breadthFirstSearch(graph, source):
    queue = [source]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current, end=' ')
        for neighboor in graph[current]:
            queue.append(neighboor)


def hasPath(graph, source, destination):
    # if source in visited:
    #     return False
    queue = [source]
    while len(queue) > 0:
        current = queue.pop(0)
        if current == destination:
            return True
        for neighboor in graph[current]:
            queue.append(neighboor)
    return False


def hasPathRecursive(graph, source, destination, visited):
    if source in visited:
        return False
    visited.add(source)
    if source == destination:
        return True
    for neighboor in graph[source]:
        if hasPathRecursive(graph, neighboor, destination, visited):
            return True
    return False

# Undirected Graph:


def undirectedGraph(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    return hasPathRecursive(graph, nodeA, nodeB, set())


def buildGraph(edges):
    graph = {}
    for edge in edges:
        [a, b] = edge
        if not a in graph:
            graph[a] = []
        if not b in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]


def connectedComonentsCount(graph):
    visited = set()
    count = 0
    for node in graph:
        if (explore(graph, node, visited)):
            count += 1
    return count


def explore(graph, current, visited):
    if current in visited:
        return False
    visited.add(current)
    for neighboor in graph[current]:
        explore(graph, neighboor, visited)
    return True


if __name__ == '__main__':
    graph1 = {  # directed graph
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': [],
        'e': ['b'],
        'f': ['d']}
    graph2 = {  # directed graph
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': [], }
    graph3 = {  # directed graph, cycled
        'a': ['b'],
        'b': ['c'],
        'c': ['a']
    }
    # print(connectedComonentsCount(graph3))
    print(connectedComonentsCount(buildGraph(edges)))

    # print('Depth First Search: ')
    # depthFirstSearchRecursive(graph2, 'a')
    # print('\nBreath First Search: ')
    # breadthFirstSearch(graph2, 'a')
    # print(f'A to B, Has path?: {hasPath(graph2, "a", "b")}')
    # print(f'A to F, Has path?: {hasPath(graph2, "a", "f")}')
