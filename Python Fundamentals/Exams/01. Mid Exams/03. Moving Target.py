def if_index_exist(index, target):
    if index in range(target):
        return True
    return False


targets = [int(number) for number in input().split()]
command = input()

while not command == "End":
    current_command, index, data = command.split()
    index = int(index)
    data = int(data)
    if current_command == "Shoot":
        if if_index_exist(index, len(targets)):
            targets[index] -= data
            if targets[index] <= 0:
                targets.pop(index)
    elif current_command == "Add":
        if index in range(len(targets)):
            targets.insert(index, data)
        else:
            print("Invalid placement!")
    elif current_command == "Strike":
        left_index = index - data
        right_index = index + data
        if index in range(len(targets)) and if_index_exist(left_index, len(targets)) and if_index_exist(right_index, len(targets)):
            left_un = targets[:left_index]
            right_un = targets[right_index+1:]
            targets = left_un + right_un
        else:
            print("Strike missed!")

    command = input()
print(f"{'|'.join([str(el) for el in targets])}")
