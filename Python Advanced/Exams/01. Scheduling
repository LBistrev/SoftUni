from collections import deque

jobs_as_nums = [int(x) for x in input().split(", ")]
searched_index = int(input())
jobs_cycles = deque(sorted([index_value for index_value in enumerate(jobs_as_nums)], key=lambda x: x[1]))
total = 0
while jobs_cycles:
    current_index, value = jobs_cycles.popleft()
    total += value
    if current_index == searched_index:
        print(total)
        break
