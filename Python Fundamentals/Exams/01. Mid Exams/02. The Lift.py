people = int(input())
max_people_on_lift = 4
current_state = [int(el) for el in input().split(" ")]
for index in range(len(current_state)):
    if current_state[index] == 0:
        if people <= 4:
            if current_state[index] <= 4:
                current_state[index] += people
                people -= people
            break
        people -= 4
        current_state[index] = 4
        if people == 0:
            break
    else:
        current_people = max_people_on_lift - current_state[index]
        current_state[index] += current_people
        people -= current_people

if people == 0 and sum(current_state) == len(current_state) * 4:
    print(f"{' '.join([str(el) for el in current_state])}")
    # for peop in current_state:
    #     if 0 <= peop < 4:
    #         print(f"The lift has empty spots!")
    #         print(f"{' '.join([str(el) for el in current_state])}")
elif people == 0:
    print(f"The lift has empty spots!")
    print(f"{' '.join([str(el) for el in current_state])}")
else:
    print(f"There isn't enough space! {people} people in a queue!")
    print(f"{' '.join([str(el) for el in current_state])}")
