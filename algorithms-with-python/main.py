def read_lab(n, m):
    sub_matrix = []
    for i in range(n):
        sub_matrix.append([el for el in input().split()])

    return sub_matrix


rows = int(input())
cols = int(input())

lab = read_lab(rows, cols)


def is_inbound(lab, row, col):
    if lab[row][col] >= len(lab):
        return True


def find_path(row, col, direction, matrix, path):
    if not is_inbound(lab, row, col):
        print('Yes')
