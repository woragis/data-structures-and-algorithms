# networks
# types of graphs:
#   undirected graph, no edge orientation
#   directed graph / digraph, edges have direction
#   weighted graph, come in directed or undirected
# special graphs:
#   trees
#   directed acycled graphs DAGS
#   bipartite graph
#   complete graph

# shortest path algorithms:
#   BFS (unweighted graph)
#   Dijkstra's Algorithm
#   Bellman-Ford
#   Floyd-Warshall
#   A*
#   and many more

# Connectivity:
#   any search algorithm
#   DFS or BFS

# Negative cycles:
#   Bellman-Ford
#   Floyd-Warshall

# Strong Connected Components
#   Tarjan's Algorithm
#   Kosaraju's Algorithm

# Traveling salesman problem
#   Held-Karp
#   Branch and bound
#   and many aproximation algorithms

# Articulation points
# Minimum spanning tree (MST)
#   Kruskal's Algorithm
#   Prim's & Boruvka's Algorithm

# Network flow / maximum flow
#   Ford-Fulkerson
#   Edmonds-Karp
#   Dicnic's Algorithm

# style
style_bright = '\033[1m'
style_dim = '\033[2m'
style_normal = '\033[22m'
style_reset = '\033[0m'
# colors
color_black = '\033[30m'
color_red = '\033[31m'
color_creen = '\033[32m'
color_yellow = '\033[33m'
color_blue = '\033[34m'
color_magenta = '\033[35m'
color_cyan = '\033[36m'
color_white = '\033[37m'
color_reset = '\033[39m'
# background
background_color_black = '\033[30m'
background_color_red = '\033[31m'
background_color_creen = '\033[32m'
background_color_yellow = '\033[33m'
background_color_blue = '\033[34m'
background_color_magenta = '\033[35m'
background_color_cyan = '\033[36m'
background_color_white = '\033[37m'
background_color_reset = '\033[39m'
# local variables
algorithm_name_color = color_cyan
algorithm_name_color_end = color_reset
algorithm_description_color = color_black

print(f'{color_blue}Most common graph algorithms:{color_reset}')
print(f'{algorithm_name_color}DFS{algorithm_name_color_end} - Depth First Search {algorithm_description_color}(stack for iterative or call stack for recursive)')
print(f'{algorithm_name_color}BFS{algorithm_name_color_end} - Breadth First Search {algorithm_description_color}(queue and iterative)')
print(f'{algorithm_name_color}Union Find{algorithm_name_color_end}')
print(f'{algorithm_name_color}Topological Sort{algorithm_name_color_end} - {algorithm_description_color}alien dict')
print(f'{algorithm_name_color}Dijksta\'s Shortest Path Algorithm{algorithm_name_color_end} {algorithm_description_color}(min-heap or priority queue) network delay time')
print(f'{algorithm_name_color}Prim and Kruskal{algorithm_name_color_end} - {algorithm_description_color}(minimum spanning tree)')
print(f'{algorithm_name_color}Floyd Warshall\'s algorithms{algorithm_name_color_end}')
