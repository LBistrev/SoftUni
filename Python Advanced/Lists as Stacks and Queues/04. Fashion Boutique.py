stack = [int(num) for num in input().split()]
capacity = int(input())

total_count = 1
weight = 0
while stack:
    current_rack = stack.pop()
    if current_rack + weight > capacity:
        total_count += 1
        weight = 0
    weight += current_rack


print(total_count)