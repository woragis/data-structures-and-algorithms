class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def __str__(self) -> str:
        print(self.graph)
        return f'{self.graph}'

    def insertNode(self, node, edges: list):
        if node not in self.graph:
            self.graph[node] = edges
        else:
            for edge in edges:
                self.graph[node].append(edge)
                if edge not in self.graph:
                    self.insertNode(edge, [])

    def bfs(self, root):
        queue = [root]
        visited = set()
        while len(queue) > 0:
            curr = queue.pop(0)
            if curr not in visited:
                print(curr)
                visited.add(curr)
                for n in self.graph[curr]:
                    queue.append(n)

    def dfs(self, root):
        stack = [root]
        visited = set()
        while len(stack) > 0:
            curr = stack.pop()
            if curr not in visited:
                print(curr)
                visited.add(curr)
                for n in self.graph[curr]:
                    stack.append(n)


myGraph = Graph()
myGraph.insertNode(1, [2])
myGraph.insertNode(1, [2, 4])
myGraph.insertNode(2, [])
myGraph.insertNode(3, [])
myGraph.insertNode(4, [])
myGraph.insertNode(4, [2, 5, 8])
# myGraph.insertNode(4, [8, 9])
# myGraph.insertNode(5, [])
# myGraph.insertNode(6, [])
# myGraph.insertNode(7, [])
# myGraph.insertNode(8, [])
# myGraph.insertNode(9, [])
# print('BFS:')
myGraph.bfs(1)
# print('DFS:')
# myGraph.dfs(1)
