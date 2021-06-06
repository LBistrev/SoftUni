def create_matrix(num1, num2):
    sublist = []
    for i in range(num1):
        sublist.append([int(el) for el in input().split()])

    return sublist


rows, cols = input().split()
rows, cols = int(rows), int(cols)

matrix = create_matrix(rows, cols)
max_sum = 0
submatrix_position = None

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = sum([matrix[row][col], matrix[row][col+1], matrix[row][col+2],
                       matrix[row+1][col], matrix[row+1][col+1], matrix[row+1][col+2],
                       matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2]
                       ])
        if current_sum >= max_sum:
            max_sum = current_sum
            submatrix_position = (row, col)

i, j = submatrix_position

print(f"Sum = {max_sum}")
print(matrix[i][j], matrix[i][j+1], matrix[i][j+2])
print(matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j+2])
print(matrix[i+2][j], matrix[i+2][j+1], matrix[i+2][j+2])

