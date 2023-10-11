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


def largestComponent(graph):
    visited = set()
    longest = 0
    for node in graph:
        size = exploreSize(graph, node, visited)
        if size > longest:
            longest = size
    return longest


def exploreSize(graph, node, visited):
    if node in visited:
        return 0
    visited.add(node)
    size = 1
    for neighbor in graph[node]:
        size += exploreSize(graph, neighbor, visited)
    return size


def shortestPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    visited = set(nodeA)
    queue = [[nodeA, 0]]

    while len(queue) > 0:
        [node, distance] = queue.pop(0)
        if node == nodeB:
            return distance
        for neighbor in graph[node]:
            if not neighbor in visited:
                visited.add(neighbor)
                queue.append([neighbor, distance+1])
    return -1


def islandCount(grid):
    visited = set()
    island_count = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if (_explore(grid, row, column, visited)):
                island_count += 1

    return island_count


def _explore(grid, row, column, visited) -> bool:
    rowInbounds = 0 <= row and row < len(grid)
    colInbounds = 0 <= column and column < len(grid[0])

    if not rowInbounds or not colInbounds:
        return False
    if grid[row][column] == 'W':
        return False

    pos = f'{row},{column}'
    if pos in visited:
        return False
    visited.add(pos)
    _explore(grid, row-1, column, visited)
    _explore(grid, row+1, column, visited)
    _explore(grid, row, column-1, visited)
    _explore(grid, row, column+1, visited)
    return True


def minimumIsland(grid):
    import math
    visited = set()
    min_size = 123421234  # use max big int size
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            size = _exploreSize(grid, row, column, visited)
            if size > 0 and size < min_size:
                min_size = size
    return min_size


def _exploreSize(grid, row, column, visited: set):
    rowInbounds = 0 <= row and row <= len(grid)
    colInbounds = 0 <= column and row <= len(grid[0])
    if not rowInbounds or not colInbounds:
        return 0
    if grid[row][column] == 'w':
        return 0
    pos = f'{row},{column}'
    if pos in visited:
        return 0
    visited.add(pos)
    size = 1
    size += _exploreSize(grid, row-1, column, visited)
    size += _exploreSize(grid, row+1, column, visited)
    size += _exploreSize(grid, row, column-1, visited)
    size += _exploreSize(grid, row, column+1, visited)
    return size


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
    edges = [
        ['i', 'j'],
        ['k', 'i'],
        ['m', 'k'],
        ['k', 'l'],
        ['o', 'n']
    ]
    numberGraph = [
        [1, 2],
        [2, 3],
        [4, 5],
        [5, 3]
    ]
    myGraph = buildGraph(numberGraph)
    largest = largestComponent(myGraph)
    shortestPath = shortestPath(edges, 'i', 'l')
    print(shortestPath)

    # print('Depth First Search: ')
    # depthFirstSearchRecursive(graph2, 'a')
    # print('\nBreath First Search: ')
    # breadthFirstSearch(graph2, 'a')
    # print(f'A to B, Has path?: {hasPath(graph2, "a", "b")}')
    # print(f'A to F, Has path?: {hasPath(graph2, "a", "f")}')
