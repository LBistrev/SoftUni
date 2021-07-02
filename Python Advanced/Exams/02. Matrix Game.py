def create_matrix_and_find_player(n):
    field = []
    player_positions = None
    for i in range(n):
        field.append(list(input()))
        if "P" in field[i]:
            player_positions = i, field[i].index("P")

    return field, player_positions


def are_indexes_valid(index1, index2, board):
    if 0 <= index1 < len(board) and 0 <= index2 < len(board):
        return True
    return False


some_text = input()
num = int(input())

matrix, player_position = create_matrix_and_find_player(num)

player_directions = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
                    }

number_of_commands = int(input())
for _ in range(number_of_commands):
    current_row, current_col = player_position
    command = input()

    if command in player_directions:
        next_row = current_row + player_directions[command][0]
        next_col = current_col + player_directions[command][1]
        if are_indexes_valid(next_row, next_col, matrix):
            if matrix[next_row][next_col] == "-":
                matrix[current_row][current_col] = "-"
                matrix[next_row][next_col] = "P"
            else:
                some_text += matrix[next_row][next_col]
                matrix[current_row][current_col] = "-"
                matrix[next_row][next_col] = "P"
            player_position = next_row, next_col
        else:
            some_text = some_text[:-1]
print(some_text)
[print(''.join(row)) for row in matrix]
