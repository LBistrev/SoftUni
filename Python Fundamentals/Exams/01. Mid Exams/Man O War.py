def is_index_valid(current_index, current_data):
    if current_index in range(len(current_data)):
        return True
    return False


status_pirate_ship = [int(el) for el in input().split(">")]
status_warship = [int(el) for el in input().split(">")]
max_health = int(input())
is_sink = False
commands = input()
while not commands == "Retire":
    data = commands.split()
    if data[0] == "Fire":
        index = int(data[1])
        damage = int(data[2])
        if is_index_valid(index, status_warship):
            status_warship[index] -= damage
            if status_warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                is_sink = True
                break
    elif data[0] == "Defend":
        start_index = int(data[1])
        end_index = int(data[2])
        damage = int(data[3])
        if is_index_valid(start_index, status_pirate_ship) and is_index_valid(end_index, status_pirate_ship):
            for attack in range(start_index, end_index+1):
                status_pirate_ship[attack] -= damage
                if status_pirate_ship[attack] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_sink = True
                    break
    elif data[0] == "Repair":
        index = int(data[1])
        health = int(data[2])
        if is_index_valid(index, status_pirate_ship):
            if status_pirate_ship[index] + health > max_health:
                status_pirate_ship[index] = max_health
            else:
                status_pirate_ship[index] += health
    elif data[0] == "Status":
        need_repair = 0
        for el in status_pirate_ship:
            if el < max_health * 0.20:
                need_repair += 1
        print(f"{need_repair} sections need repair.")

    commands = input()
if not is_sink:
    if sum(status_pirate_ship) and sum(status_warship):
        print(f"Pirate ship status: {sum(status_pirate_ship)}")
        print(f"Warship status: {sum(status_warship)}")
