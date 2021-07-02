import math


def create_matrix_and_find_player(n):
    field = []
    player_pos = None
    for i in range(n):
        field.append(input().split())
        if "P" in field[i]:
            player_pos = i, field[i].index("P")

    return field, player_pos


def is_index_valid(index1, index2, field):
    if 0 <= index1 < len(field) and 0 <= index2 < len(field):
        return True
    return False


rows = int(input())
matrix, player_position = create_matrix_and_find_player(rows)

directions = {
            "up": (-1, 0),
            "right": (0, 1),
            "down": (1, 0),
            "left": (0, -1),
}
game_over = False
sum_coins = 0
player_directions = []
while not game_over:
    if sum_coins >= 100:
        break
    command = input()

    current_row, current_col = player_position
    if command in directions:
        next_row_pos = current_row + directions[command][0]
        next_col_pos = current_col + directions[command][1]
        if is_index_valid(next_row_pos, next_col_pos, matrix):
            if matrix[next_row_pos][next_col_pos] == "X":
                game_over = True
                sum_coins = math.floor(sum_coins - sum_coins * 0.5)
                break
            coins = int(matrix[next_row_pos][next_col_pos])
            sum_coins += coins
            player_position = next_row_pos, next_col_pos
            player_directions.append((next_row_pos, next_col_pos))
        else:
            sum_coins = math.floor(sum_coins - sum_coins * 0.5)
            game_over = True

if game_over:
    print(f"Game over! You've collected {sum_coins} coins.")
else:
    print(f"You won! You've collected {sum_coins} coins.")

print("Your path:")
[print(list(x)) for x in player_directions]
