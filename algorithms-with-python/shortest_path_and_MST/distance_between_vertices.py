from collections import deque


def find_shortest_path(graph, source, destination):
    queue = deque([source])
    visited = {source}

    parent = {source: None}

    while queue:
        node = queue.popleft()
        if node == destination:
            break
        for child in graph[node]:
            if child in visited:
                continue
            queue.append(child)
            visited.add(child)
            parent[child] = node
    return parent


def find_path_size(parent, destination):
    node = destination
    size = 0
    while node is not None:
        node = parent[node]
        size += 1

    return size - 1


nodes = int(input())
pairs = int(input())

graph = {}

for _ in range(nodes):
    node_str, children_str = input().split(':')
    node = int(node_str)
    children = [int(x) for x in children_str.split()] if children_str else []
    graph[node] = children

for _ in range(pairs):
    source, destination = [int(x) for x in input().split('-')]

    parent = find_shortest_path(graph, source, destination)
    if destination not in parent:
        print(f'{{{source}, {destination}}} -> -1')
        continue

    size = find_path_size(parent, destination)

    print(f'{{{source}, {destination}}} -> {size}')

# Examples
"""
    2
    2
    1:2  ->  {1, 2} ->  1
    2:   ->  {2, 1} -> -1
    1-2
    2-1

---------------------------

    8
    4
    1:4
    2:4
    3:4 5     ->   {1, 6} ->  2
    4:6       ->   {1, 5} -> -1
    5:3 7 8   ->   {5, 6} ->  3
    6:        ->   {5, 8} ->  1
    7:8
    8:
    1-6
    1-5
    5-6
    5-8

---------------------------

    9
    8
    11:4
    4:12 1
    1:12 21 7
    7:21
    12:4 19    ->    {11, 7}   ->  3
    19:1 21    ->    {11, 21}  ->  3
    21:14 31   ->    {21, 4}   -> -1
    14:14      ->    {19, 14}  ->  2
    31:        ->    {1, 4}    ->  2
    11-7       ->    {1, 11}   -> -1
    11-21      ->    {31, 21}  -> -1
    21-4       ->    {11, 14}  ->  4
    19-14
    1-4
    1-11
    31-21
    11-14

"""
