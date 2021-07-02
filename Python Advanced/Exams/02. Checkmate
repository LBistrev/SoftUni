def create_matrix_and_find_the_king(n):
    sub_matrix = []
    king_positions = None
    for i in range(n):
        sub_matrix.append(input().split())
        if "K" in sub_matrix[i]:
            king_positions = i, sub_matrix[i].index("K")

    return sub_matrix, king_positions


def are_indexes_valid(index1, index2, board):
    if 0 <= index1 < len(board) and 0 <= index2 < len(board):
        return True
    return False


rows = 8
matrix, king_position = create_matrix_and_find_the_king(rows)

directions = {
    "up": (-1, 0),
    "up_right": (-1, 1),
    "right": (0, 1),
    "down_right": (1, 1),
    "down": (1, 0),
    "down_left": (1, -1),
    "left": (0, -1),
    "up_left": (-1, -1),
            }
start_row, start_col = king_position
queens_positions = []
game_over = False

for direction in directions:
    next_row = start_row + directions[direction][0]
    next_col = start_col + directions[direction][1]
    
    while are_indexes_valid(next_row, next_col, matrix):
        if matrix[next_row][next_col] == "Q":
            queens_positions.append((next_row, next_col))
            game_over = True
            break
        next_row += directions[direction][0]
        next_col += directions[direction][1]

if game_over:
    [print(list(x)) for x in queens_positions]
else:
    print("The king is safe!")
