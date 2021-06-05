number = int(input())
chemicals = set()
for _ in range(number):
    chemicals = chemicals.union(set(input().split()))

[print(el) for el in chemicals]