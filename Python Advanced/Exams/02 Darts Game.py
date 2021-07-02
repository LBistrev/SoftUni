def create_matrix(n):
    sub_matrix = []
    for i in range(n):
        sub_matrix.append(input().split())

    return sub_matrix


def are_indexes_valid(index1, index2, board):
    if index1 in range(7) and index2 in range(7):
        return True
    return False


first_player, second_player = input().split(", ")
players_dict = {first_player: 501, second_player: 501}
players_count = {first_player: 0, second_player: 0}
matrix = create_matrix(7)
is_winner = False
while not is_winner:
    for player, value in players_dict.items():
        index_row, index_col = [int(x) for x in input()[1: -1].split(", ")]
        players_count[player] += 1
        if are_indexes_valid(index_row, index_col, matrix):
            el = matrix[index_row][index_col]
            if el.isdigit():
                players_dict[player] -= int(el)

            elif el == "T":
                sum_points = sum([int(matrix[index_row][0]), int(matrix[index_row][-1]), int(matrix[0][index_col]),
                         int(matrix[-1][index_col])])
                players_dict[player] -= sum_points * 3
            elif el == "D":
                sum_points = sum([int(matrix[index_row][0]), int(matrix[index_row][-1]), int(matrix[0][index_col]),
                                  int(matrix[-1][index_col])])
                players_dict[player] -= sum_points * 2
            elif el == "B":
                players_dict[player] -= 501
        if players_dict[player] <= 0:
            print(f"{player} won the game with {players_count[player]} throws!")
            is_winner = True
            break




