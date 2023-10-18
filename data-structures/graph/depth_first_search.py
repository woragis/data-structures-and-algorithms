# recursive
def walk(tree):
    if tree:
        print(tree)  # pre-order
        walk(tree.left)
        # print(tree)  # in-order
        walk(tree.right)
        # print(tree)  # post-order


def walk2(tree, stack: list):
    # iterative
    # faster, cause it doesn't rely on the call stack
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop()
        if node:
            print(node)  # pre-order
            stack.append(node.left)
            # print(node)  # in-order
            stack.append(node.right)
            # print(node)  # post-order


class Graph:
    def __init__(self) -> None:
        self.graph = {}
        # self.root = 'A'
        self.size = 0

    def insert(self, target, neighbors):
        if target not in self.graph:
            self.graph[target] = neighbors
        else:
            for j in neighbors:
                self.graph[target].append(j)
                self.insert(j, [])

    def traverse(self, current, visited=set()):
        if not current in visited:
            visited.add(current)
            print(current)
            for neighbor in self.graph[current]:
                self.traverse(neighbor, visited)
        else:
            return

    def dfs(self, current, target, visited=set()):
        if current in visited:
            return
        visited.add(current)
        for neighbor in current:
            self.dfs(neighbor, target, visited)

    def dfs_iterative(self, target):
        stack = [self.root]
        visited = set()
        while len(stack) > 0:
            current = stack.pop()
            if current not in visited:
                for neighbors in current:
                    stack.append(neighbors)


def depthFirstSearch_Recursive(graph, current, visited: set = set()):
    # uses recursion thus the call stack
    if current not in visited:
        print(current)
        visited.add(current)
        for neighbor in graph[current]:
            depthFirstSearch_Recursive(graph, neighbor, visited)


def depthFirstSearch_Iterative(graph, node):
    visited = set()
    stack = [node]
    while len(stack) > 0:
        cur = stack.pop()
        if cur not in visited:
            visited.add(cur)
            print(cur)
            for neighbor in reversed(range(len(graph[cur]))):
                stack.append(graph[cur][neighbor])


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
    '''
    newGraph = Graph()
    newGraph.insert('A', ['B', 'C'])
    newGraph.insert('B', ['A', 'D', 'E'])
    newGraph.insert('C', ['B', 'F', 'G'])
    newGraph.insert('D', [])
    newGraph.insert('E', [])
    newGraph.insert('F', [])
    newGraph.insert('G', [])
    newGraph.insert('Z', [])
    newGraph.traverse('A')'''
    # mySet = set()
    # depthFirstSearch_Recursive(graph, 'A', mySet)
    depthFirstSearch_Iterative(graph, 'A')
