def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


number_of_towns = int(input())
number_of_streets = int(input())

graph = []

for _ in range(number_of_streets):
    first, second, cost = [int(x) for x in input().split(' - ')]
    graph.append((first, second, cost))

sorted_graph = sorted(graph, key=lambda x: x[2])
parent = [num for num in range(number_of_streets)]
total_cost = 0

for first, second, weight in sorted_graph:
    first_node_root = find_root(parent, first)
    second_node_root = find_root(parent, second)

    if first_node_root == second_node_root:
        continue
    parent[first_node_root] = second_node_root
    total_cost += weight
    # print(first, second, weight)

print(f'Total cost: {total_cost}')

# EXAMPLES

"""
    Input               Output

    4
    5
    0 - 1 - 10
    0 - 2 - 6     ->    Total cost: 19
    0 - 3 - 5
    1 - 3 - 15
    2 - 3 - 4

"""
