from pprint import pprint


def get_magic_triangle(n):
    triangle_matrix = []
    for i in range(n):
        triangle_matrix.append([0] * (i + 1))

    for index_row, row in enumerate(triangle_matrix):
        for index_col, col in enumerate(row):
            up_left = up_right = 0
            triangle_matrix[index_row][index_col] = 1
            if (index_row, index_col) == (0, 0):
                continue

            if 0 <= index_row - 1 < len(triangle_matrix) and 0 <= index_col - 1 < len(triangle_matrix[index_row - 1]):
                up_left = triangle_matrix[index_row - 1][index_col - 1]

            if 0 <= index_row - 1 < len(triangle_matrix) and 0 <= index_col < len(triangle_matrix[index_row - 1]):
                up_right = triangle_matrix[index_row - 1][index_col]

            triangle_matrix[index_row][index_col] = up_left + up_right

    return triangle_matrix


matrix = get_magic_triangle(7)
pprint(matrix)

