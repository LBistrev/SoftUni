from collections import deque


def find_parent_by_node(graph, start_node, destination_node):
    visited = [False] * len(graph)
    parent = [None] * len(graph)

    visited[start_node] = True
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node == destination_node:
            break

        for child in graph[node]:
            if visited[child]:
                continue
            visited[child] = True
            queue.append(child)
            parent[child] = node

    return parent


def reconstruct_path(parent, destination_node):
    path = deque()
    node = destination_node

    while node is not None:
        path.appendleft(node)
        node = parent[node]

    return path


nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes + 1)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())
destination_node = int(input())
parent = find_parent_by_node(graph, start_node, destination_node)
path = reconstruct_path(parent, destination_node)

print(f'Shortest path length is: {len(path) - 1}')
print(*path, sep=' ')

# Examples
"""
    8
    10
    1 2
    1 4
    2 3
    4 5
    5 8   -> Shortest path length is: 3
    5 6   -> 1 4 5 7
    5 7
    5 8
    6 7
    7 8
    1
    7

---------------------------

    11
    11
    1 5
    1 4
    5 7
    7 8
    8 2   -> Shortest path length is: 2
    2 3   -> 6 2 3
    3 4
    4 1
    6 2
    9 10
    11 9
    6
    3

"""
