def breadthFirstSearch(graph, root, target) -> bool:
    queue = [root]
    visited = set()
    while queue:
        current = queue.pop(0)
        if current not in visited:
            print(current)
            if current == target:
                return True
            visited.add(current)
            for neighbor in graph[current]:
                queue.append(neighbor)
    return False


if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['E', 'G'],
        'E': ['X', 'Y', 'Z'],
        'F': ['W'],
        'G': [],
        'X': [],
        'Y': [],
        'Z': [],
        'W': []
    }
    breadthFirstSearch(graph, 'A', 'C')
