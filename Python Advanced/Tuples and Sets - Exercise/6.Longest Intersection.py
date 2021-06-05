number = int(input())

result = []

for _ in range(number):
    first_line, second_line = input().split("-")
    first_line = first_line.split(",")
    second_line = second_line.split(",")
    first_line = (int(first_line[0]), int(first_line[1]))
    second_line = (int(second_line[0]), int(second_line[1]))
    first_range = range(int(first_line[0]), int(first_line[1]+1))
    second_range = range(int(second_line[0]), int(second_line[1]+1))
    intersection = set(first_range).intersection(second_range)
    result.append(intersection)

longest_intersection = sorted(result, key=lambda x: -len(x))[0]

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
