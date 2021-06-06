def create_matrix(n, m):
    sub_matrix = []
    for i in range(n):
        sub_matrix.append([])
        for j in range(m):
            sub_matrix[-1].append("")

    return sub_matrix


rows, cols = [int(el) for el in input().split()]
text = input()

matrix = create_matrix(rows, cols)
index = 0

for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            if index + 1 == len(text)+1:
                index = 0
            matrix[row][col] = text[index]
            index += 1
    else:
        for col in range(cols-1, -1, -1):
            if index + 1 == len(text)+1:
                index = 0
            matrix[row][col] = text[index]
            index += 1

    print(''.join(matrix[row]))
