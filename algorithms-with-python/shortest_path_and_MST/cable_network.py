from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


budget = int(input())
number_of_nodes = int(input())
number_of_edges = int(input())

graph = []
[graph.append([]) for _ in range(number_of_nodes)]
tree = set()
budget_used = 0
pq = PriorityQueue()

for _ in range(number_of_edges):
    edge_data = input().split()
    first, second, weight = int(edge_data[0]), int(edge_data[1]), int(edge_data[2])
    graph[first].append(Edge(first, second, weight))
    graph[second].append(Edge(first, second, weight))
    if len(edge_data) == 4:
        tree.add(first)
        tree.add(second)

for node in tree:
    for edge in graph[node]:
        pq.put(edge)

while not pq.empty():
    min_edge = pq.get()
    non_tree_node = None

    if min_edge.first in tree and min_edge.second not in tree:
        non_tree_node = min_edge.second

    elif min_edge.first not in tree and min_edge.second in tree:
        non_tree_node = min_edge.first

    if non_tree_node is None:
        continue

    if budget_used + min_edge.weight > budget:
        break

    budget_used += min_edge.weight
    tree.add(non_tree_node)

    for edge in graph[non_tree_node]:
        pq.put(edge)

print(f'Budget used: {budget_used}')


# EXAMPLES

"""
    Input                       Output
    
    20
    9
    15
    1 4 8
    4 0 6 connected
    1 7 7
    4 7 10
    4 8 3
    7 8 4
    0 8 5 connected     ->  Budget used: 13
    8 6 9
    8 3 20 connected
    0 5 4
    0 3 9 connected
    6 3 8
    6 2 12
    5 3 2
    3 2 14 connected

--------------------------------------------

    7
    4
    5
    0 1 9
    0 3 4 connected     ->  Budget used: 5
    3 1 6
    3 2 11 connected
    1 2 5

--------------------------------------------

    20
    8
    16
    0 1 4
    0 2 5
    0 3 1 connected
    1 2 8
    1 3 2
    2 3 3
    2 4 16
    2 5 9              ->  Budget used: 12
    3 4 7
    3 5 14
    4 5 12
    4 6 22
    4 7 9
    5 6 6
    5 7 18
    6 7 15

"""
