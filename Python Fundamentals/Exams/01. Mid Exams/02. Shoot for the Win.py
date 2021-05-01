the_targets = [int(num) for num in input().split()]

command = input()
counter = 0
while not command == "End":
    reduced_list = []
    index = int(command)
    if index not in range(len(the_targets)):
        command = input()
        continue
    shoot = the_targets[index]
    if shoot == -1:
        command = input()
        continue

    the_targets[index] = -1
    counter += 1
    for current_target in range(len(the_targets)):
        if the_targets[current_target] == -1:
            continue
        if the_targets[current_target] > shoot:
            the_targets[current_target] -= shoot
        else:
            the_targets[current_target] += shoot
    command = input()
the_targets = [str(string) for string in the_targets]
print(f"Shot targets: {counter} -> {' '.join(the_targets)}")
