initial_loot = input().split("|")
new_list = []
command = input()

while not command == "Yohoho!":
    current_command = command.split()
    if current_command[0] == "Loot":
        for item in range(1, len(current_command)):
            if current_command[item] not in initial_loot:
                initial_loot.insert(0, current_command[item])

    elif current_command[0] == "Drop":
        if int((current_command[1])) in range(len(initial_loot)):
            el = initial_loot[int(current_command[1])]
            initial_loot.pop(int(current_command[1]))
            initial_loot.append(el)
    elif current_command[0] == "Steal":
        count = int(current_command[1])
        if len(initial_loot) <= count:
            print(f"{', '.join(initial_loot)}")
            initial_loot.clear()
        else:
            removed_items = initial_loot[-count:]
            del initial_loot[-count:]
            print(f"{', '.join(removed_items)}")
    command = input()

if len(initial_loot) <= 0:
    print("Failed treasure hunt.")
else:
    sum_of_all_items = len(''.join(initial_loot))
    avg = sum_of_all_items / len(initial_loot)
    print(f"Average treasure gain: {avg:.2f} pirate credits.")
