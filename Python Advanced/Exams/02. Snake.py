def create_matrix_and_find_snake_position(n):
    sub_matrix = []
    position = None
    for index in range(n):
        sub_matrix.append(list(input()))
        if "S" in sub_matrix[index]:
            position = index, sub_matrix[index].index("S")
    return sub_matrix, position


def search_lair(symbol, territory):
    for i in range(len(territory)):
        for j in range(len(territory)):
            if territory[i][j] == symbol:
                return i, j


def are_indexes_valid(index1, index2, territory):
    if 0 <= index1 < len(territory) and 0 <= index2 < len(territory):
        return True
    return False


rows = int(input())
snake_territory, snake_position = create_matrix_and_find_snake_position(rows)
current_row, current_col = snake_position
food_quantity = 0
game_over = False

directions = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
            }

while not game_over:
    if food_quantity >= 10:
        break
    command = input()
    current_row, current_col = snake_position
    if command in directions:
        next_row = current_row + directions[command][0]
        next_col = current_col + directions[command][1]
        snake_territory[current_row][current_col] = "."
        if are_indexes_valid(next_row, next_col, snake_territory):
            if snake_territory[next_row][next_col] == "*":
                food_quantity += 1
                snake_territory[next_row][next_col] = "S"
            elif snake_territory[next_row][next_col] == "B":
                snake_territory[next_row][next_col] = "."
                searched_row, searched_col = search_lair("B", snake_territory)
                snake_territory[searched_row][searched_col] = "S"
                next_row, next_col = searched_row, searched_col
            else:
                snake_territory[next_row][next_col] = "S"
            snake_position = next_row, next_col
        else:
            game_over = True


if game_over:
    print("Game over!")

elif food_quantity >= 10:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_quantity}")
[print(''.join(row)) for row in snake_territory]
