def dfs(parent, row, col, matrix, visited_places_matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return

    if visited_places_matrix[row][col]:
        return

    if matrix[row][col] != parent:
        return

    visited_places_matrix[row][col] = True
    dfs(parent, row - 1, col, matrix, visited_places_matrix)
    dfs(parent, row + 1, col, matrix, visited_places_matrix)
    dfs(parent, row, col - 1, matrix, visited_places_matrix)
    dfs(parent, row, col + 1, matrix, visited_places_matrix)


rows = int(input())
cols = int(input())

matrix = []
visited_places_matrix = []
areas = {}
total_areas = 0

for _ in range(rows):
    matrix.append(list(input()))
    visited_places_matrix.append([False] * cols)

for row in range(rows):
    for col in range(cols):
        if visited_places_matrix[row][col]:
            continue
        key = matrix[row][col]
        dfs(key, row, col, matrix, visited_places_matrix)
        if key not in areas:
            areas[key] = 1
        else:
            areas[key] += 1
        total_areas += 1

print(f'Areas: {total_areas}')
for area, size in sorted(areas.items()):
    print(f"Letter '{area}' -> {size}")


# Examples
"""
    6
    8
    aacccaac
    baaaaccc
    baabaccc
    bbdaaccc
    ccdccccc
    ccdccccc
    
---------------------------

    5
    9
    asssaadas
    adsdasdad
    sdsdadsas
    sdasdsdsa
    ssssasddd

"""