def create_matrix(n):
    sub_matrix = []
    for i in range(n):
        sub_matrix.append(list())
        for j in range(n):
            sub_matrix[i].append([""])

    return sub_matrix


def are_indexes_valid(sequence, index):
    if 0 <= index < len(matrix):
        return True
    return False


num = int(input())
bombs = int(input())
bomb_mark = "*"
matrix = create_matrix(num)

bombs_count = 0

for i in range(bombs):
    bombs_rows, bombs_cols = [int(el) for el in input()[1:-1].split(", ")]
    if are_indexes_valid(matrix, bombs_rows) and are_indexes_valid(matrix, bombs_cols):
        matrix[bombs_rows][bombs_cols] = bomb_mark

for row in range(num):
    for col in range(num):
        directions = [
            (row - 1, col),
            (row - 1, col + 1),
            (row, col + 1),
            (row + 1, col + 1),
            (row + 1, col),
            (row + 1, col - 1),
            (row, col - 1),
            (row - 1, col - 1),
        ]
        if matrix[row][col] == bomb_mark:
            continue
        matrix[row][col] = 0
        for position in directions:
            i, j = position
            if are_indexes_valid(matrix, i) and are_indexes_valid(matrix, j):
                if matrix[i][j] == bomb_mark:
                    matrix[row][col] += 1

for row in matrix:
    print(' '.join([str(x) for x in row]))

