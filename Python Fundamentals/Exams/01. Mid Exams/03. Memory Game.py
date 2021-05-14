def is_index_valid(index, len_list):
    if index in range(len_list):
        return True
    return False


sequence_of_elements = input().split()
command = input()
rounds_counter = 0
while not command == "end" and sequence_of_elements:
    first_index, sec_index = command.split()
    first_index = int(first_index)
    sec_index = int(sec_index)

    rounds_counter += 1
    if is_index_valid(first_index, len(sequence_of_elements)) and is_index_valid(sec_index, len(sequence_of_elements)) and not first_index == sec_index:
        first_el = sequence_of_elements[first_index]
        sec_el = sequence_of_elements[sec_index]
        if first_el == sec_el:
            sequence_of_elements.remove(first_el)
            sequence_of_elements.remove(sec_el)
            print(f"Congrats! You have found matching elements - {first_el}!")
        else:
            print("Try again!")
    else:
        add_element = f"-{rounds_counter}a"
        center = len(sequence_of_elements) // 2
        sequence_of_elements.insert(center, add_element)
        sequence_of_elements.insert(center, add_element)
        print("Invalid input! Adding additional elements to the board")

    command = input()
if not sequence_of_elements:
    print(f"You have won in {rounds_counter} turns!")
else:
    print("Sorry you lose :(")
    print(f"{' '.join(sequence_of_elements)}")
