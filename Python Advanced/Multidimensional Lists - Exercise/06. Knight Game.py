# create_matrix
def create_matrix():
    num = int(input())
    sub_matrix = []
    for _ in range(num):
        sub_matrix.append(list(input()))

    return sub_matrix


#  find all knight positions
def find_all_knights(sub_matrix):
    knights_positions = []
    for i in range(len(sub_matrix)):
        for j in range(len(sub_matrix)):
            if sub_matrix[i][j] == "K":
                position = i, j
                knights_positions.append(position)

    return knights_positions


def knights_attacking(matrix):
    knight_position = find_all_knights(matrix)
    for row, col in knight_position:
        positions = [
            (row - 2, col + 1),
            (row - 1, col + 2),
            (row + 1, col + 2),
            (row + 2, col + 1),
            (row + 2, col - 1),
            (row + 1, col - 2),
            (row - 1, col - 2),
            (row - 2, col - 1),
        ]

        for current_position in positions:
            row, col = current_position
            if not 0 <= row < len(matrix):
                continue
            if not 0 <= col < len(matrix):
                continue
            if matrix[row][col] == "K":
                return True
    return False


#  calculate aggression (how many other knights are attacked by current)
def calculate_aggression(matrix, knight_positions):
    aggression_dict = {}
    for position in knight_positions:
        row, col = position
        positions = [
            (row - 2, col + 1),
            (row - 1, col + 2),
            (row + 1, col + 2),
            (row + 2, col + 1),
            (row + 2, col - 1),
            (row + 1, col - 2),
            (row - 1, col - 2),
            (row - 2, col - 1),
        ]
        counter_attacked = 0
        for current_row, current_col in positions:
            if not 0 <= current_row < len(matrix):
                continue
            if not 0 <= current_col < len(matrix):
                continue
            if matrix[current_row][current_col] == "K":
                counter_attacked += 1
        aggression_dict[(row, col)] = counter_attacked

    return aggression_dict


def find_max_aggression(aggression_dict):
    max_aggression = None
    max_position = None
    sorted_aggression = sorted(aggression_dict.items(), key=lambda x: -x[1])
    for key, value in sorted_aggression:
        max_position = key
        max_aggression = value

        return max_position


def main():
    matrix = create_matrix()
    max_count = 0
    while knights_attacking(matrix):
        knight_positions = find_all_knights(matrix)
        aggression_dict = calculate_aggression(matrix, knight_positions)
        row, col = find_max_aggression(aggression_dict)

        matrix[row][col] = "0"
        max_count += 1
    print(max_count)


main()

