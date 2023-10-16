# Dijkstra's Algorithm in Python

'''
import sys

# Providing the graph
vertices = [[0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0]]

edges = [[0, 0, 1, 2, 0, 0, 0],
         [0, 0, 2, 0, 0, 3, 0],
         [1, 2, 0, 1, 3, 0, 0],
         [2, 0, 1, 0, 0, 0, 1],
         [0, 0, 3, 0, 0, 2, 0],
         [0, 3, 0, 0, 2, 0, 1],
         [0, 0, 0, 1, 0, 1, 0]]

# Find which vertex is to be visited next


def to_be_visited():
    global visited_and_distance
    v = -10
    for index in range(num_of_vertices):
        if visited_and_distance[index][0] == 0 \
            and (v < 0 or visited_and_distance[index][1] <=
                 visited_and_distance[v][1]):
            v = index
    return v


num_of_vertices = len(vertices[0])

visited_and_distance = [[0, 0]]
for i in range(num_of_vertices-1):
    visited_and_distance.append([0, sys.maxsize])

for vertex in range(num_of_vertices):

    # Find next vertex to be visited
    to_visit = to_be_visited()
    for neighbor_index in range(num_of_vertices):

        # Updating new distances
        if vertices[to_visit][neighbor_index] == 1 and \
                visited_and_distance[neighbor_index][0] == 0:
            new_distance = visited_and_distance[to_visit][1] \
                + edges[to_visit][neighbor_index]
            if visited_and_distance[neighbor_index][1] > new_distance:
                visited_and_distance[neighbor_index][1] = new_distance

        visited_and_distance[to_visit][0] = 1

i = 0

# Printing the distance
for distance in visited_and_distance:
    print("Distance of ", chr(ord('a') + i),
          " from source vertex: ", distance[1])
    i = i + 1

'''

# Dijkstras algorithm from neetcode


class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], src: int) -> dict[int, int]:
        import heapq
        adj = {}
        for i in range(n):
            adj[i] = []
        for s, d, weight in edges:
            adj[s].append([d, weight])
        shortest = {}  # map vertex -> dist of shortest path
        minHeap = [[0, src]]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, n2])
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest


def dijkstra(graph, src, dest):
    import sys
    from heapq import heapify, heappush, heappop
    inf = sys.maxsize
    node_data = {
        'A': {'cost': inf, 'pred': []},
        'B': {'cost': inf, 'pred': []},
        'C': {'cost': inf, 'pred': []},
        'D': {'cost': inf, 'pred': []},
        'E': {'cost': inf, 'pred': []},
        'F': {'cost': inf, 'pred': []},
    }
    node_data[src]['cost'] = 0
    visited = set()
    temp = src
    for i in range(5):

        pass
    return


if __name__ == '__main__':
    graph = {
        'A': {'B': 2, 'C': 4},
        'B': {'A': 2, 'C': 3, 'D': 8},
        'C': {'A': 4, 'B': 3, 'E': 5, 'D': 2},
        'D': {'B': 8, 'C': 2, 'E': 11, 'F': 22},
        'E': {'C': 5, 'D': 11, 'F': 1},
        'F': {'D': 22, 'E': 1},
    }
    source = 'A'
    destination = 'F'
    dijkstra(graph, source, destination)
