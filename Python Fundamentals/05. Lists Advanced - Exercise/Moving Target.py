def is_index_valid(current_index, sequence_of_targets):
    if 0 <= current_index < len(sequence_of_targets):
        return True
    return False


targets = [int(num) for num in input().split()]
commands = input()

while not commands == "End":
    current_command, index, data = commands.split()
    index = int(index)
    if current_command == "Shoot":
        power = int(data)
        if is_index_valid(index, targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif current_command == "Add":
        value = int(data)
        if is_index_valid(index, targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif current_command == "Strike":
        radius = int(data)
        start_index = index - radius
        end_index = index + radius
        if is_index_valid(index, targets) and is_index_valid(start_index, targets) and is_index_valid(end_index, targets):
            first_part = targets[:start_index]
            second_part = targets[end_index+1:]
            targets = first_part + second_part
        else:
            print("Strike missed!")

    commands = input()

print("|".join([str(el) for el in targets]))
