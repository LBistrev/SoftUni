def dfs(node, destination, graph, visited):
    if node in visited:
        return
    visited.add(node)
    if node == destination:
        return

    for child in graph[node]:
        dfs(child, destination, graph, visited)


def path_exists(source, destination, graph):
    visited = set()

    dfs(source, destination, graph, visited)

    return destination in visited


nodes = int(input())
graph = {}
edges = []

for _ in range(nodes):
    node, children_str = input().split(' -> ')
    children = children_str.split()
    graph[node] = children
    for child in children:
        edges.append((node, child))

sorted_edges = sorted(edges, key=lambda x: (x[0], x[1]))
removed_edges = []

for source, destination in sorted_edges:
    if destination not in graph[source] or source not in graph[destination]:
        continue

    graph[source].remove(destination)
    graph[destination].remove(source)

    if path_exists(source, destination, graph):
        removed_edges.append((source, destination))
    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f'Edges to remove: {len(removed_edges)}')
[print(f'{first} - {second}') for first, second in removed_edges]


# Examples
"""
    Input                  Expected
    
    8
    1 -> 2 5 4
    2 -> 1 3
    3 -> 2 5             Edges to remove: 2
    4 -> 1       ->      1 - 2
    5 -> 1 3             6 - 7
    6 -> 7 8
    7 -> 6 8
    8 -> 6 7

---------------------------
    Input                  Expected
    14
    K -> X J
    J -> K N
    N -> J X L M
    X -> K N Y
    M -> N I
    Y -> X L               Edges to remove: 7
    L -> N I Y     ->      A - Z
    I -> M L               A - Z
    A -> Z Z Z             B - F
    Z -> A A A             E - F
    F -> E B P             I - L
    E -> F P               J - K
    P -> B F E             L - N
    B -> F P

"""