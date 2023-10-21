def shortestPath(graph, start, target):
    path_list = [[start]]
    path_index = 0
    previous_nodes = {start}
    if start == target:
        return path_list[0]
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        if target in next_nodes:
            current_path.append(target)
            return current_path
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                previous_nodes.add(next_node)

        path_index += 1
    return []


'''
def find_path_bfs(s, e, grid):
    queue = [(s, [])]  # start point, empty path

    while len(queue) > 0:
        node, path = queue.pop(0)
        path.append(node)
        mark_visited(node, v)

        if node == e:
            return path

        adj_nodes = get_neighbors(node, grid)
        for item in adj_nodes:
            if not is_visited(item, v):
                queue.append((item, path[:]))

    return None  # no path found
'''


if __name__ == '__main__':
    graph = {}
    adjancency_list = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3, 4],
        3: [1, 2, 5],
        4: [2, 5],
        5: [3, 4]
    }
    graph[1] = {2, 5}
    graph[2] = {1, 3, 5}
    graph[3] = {2, 4}
    graph[4] = {3, 5, 6}
    graph[5] = {1, 2, 4}
    graph[6] = {4}

    result = shortestPath(adjancency_list, 0, 5)
    print(result)
