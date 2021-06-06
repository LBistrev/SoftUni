def create_matrix(n, m):
    sub_matrix = []
    for i in range(n):
        sub_matrix.append([el for el in input().split()])

    return sub_matrix


def is_index_valid(num, sub_list):
    if 0 <= num <= len(sub_list):
        return True
    return False


rows, cols = [int(el) for el in input().split()]


matrix = create_matrix(rows, cols)
valid_index = True

command = input()

while not command == "END":
    current_nums = []
    current_matrix = []
    if command.startswith("swap"):
        data = command.split()
        for index in range(1, len(data)):
            if data[index].isdigit():
                current_nums.append(int(data[index]))
        if len(current_nums) < 4 or len(current_nums) > 4:
            print("Invalid input!")
        else:
            first, second, third, fourth = current_nums
            for i in current_nums:
                if not is_index_valid(i, matrix):
                    valid_index = False
                    print("Invalid input!")
                    break
            if valid_index:
                matrix[first][second], matrix[third][fourth] = matrix[third][fourth], matrix[first][second]
                for i in range(rows):
                    print(" ".join(matrix[i]))
    else:
        print("Invalid input!")

    valid_index = True

    command = input()
