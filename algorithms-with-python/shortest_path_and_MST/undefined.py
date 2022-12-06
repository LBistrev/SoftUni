from collections import deque


def find_path(parent, node):
    result = deque()
    while node is not None:
        result.appendleft(node)
        node = parent[node]

    return result


number_of_nodes = int(input())
number_of_edges = int(input())

graph = []

for _ in range(number_of_edges):
    source, destination, weight = [int(x) for x in input().split()]
    graph.append((source, destination, weight))

start_path = int(input())
end_path = int(input())

distance = [float('inf')] * (number_of_nodes + 1)
distance[start_path] = 0

parent = [None] * (number_of_nodes + 1)

for _ in range(number_of_nodes - 1):
    for first, second, weight in graph:
        if distance[first] == float('inf'):
            continue
        new_distance = distance[first] + weight
        if new_distance < distance[second]:
            distance[second] = new_distance
            parent[second] = first

for first, second, weight in graph:
    new_distance = distance[first] + weight
    if new_distance < distance[second]:
        print('Undefined')
        break
else:
    path = find_path(parent, end_path)
    print(*path, sep=' ')
    print(distance[end_path])


# EXAMPLES

"""
    Input           Output

    5
    8
    1 2 -1
    1 3 4
    2 3 3
    2 4 2    ->    1 2 5 4
    2 5 2    ->   -2
    4 2 1
    4 3 5
    5 4 -3
    1
    4

--------------------------

    5
    8
    1 2 -1
    1 3 4
    2 3 3
    2 4 2    ->    Undefined
    2 5 2
    4 2 -1
    4 3 5
    5 4 -3
    1
    4

"""
