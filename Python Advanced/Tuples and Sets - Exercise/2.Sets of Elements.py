n, m = input().split()
n, m = int(n), int(m)

set_a, set_b = set(), set()

for _ in range(n):
    set_a.add(input())

for _ in range(m):
    set_b.add(input())

result = set_a.intersection(set_b)

[print(el) for el in result]
