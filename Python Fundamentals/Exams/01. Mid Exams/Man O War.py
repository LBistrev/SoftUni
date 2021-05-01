status_pirate_ship = input().split(">")
status_battle_ship = input().split(">")
max_health = int(input())
command = input()
pirate_ship_integers = [int(n) for n in status_pirate_ship]
battle_ship_integers = [int(n) for n in status_battle_ship]
is_valid = True
while not command == "Retire":
    data = command.split()
    if data[0] == "Fire":
        index = int(data[1])
        damage = int(data[2])
        if 0 <= index < len(status_battle_ship):
            battle_ship_integers[index] -= damage
            if battle_ship_integers[index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                is_valid = False
                break
    elif data[0] == "Defend":
        start_index = int(data[1])
        end_index = int(data[2])
        damage = int(data[3])
        if 0 <= start_index < len(pirate_ship_integers) and 0 <= end_index < len(pirate_ship_integers):
            for el in range(start_index, end_index+1):
                pirate_ship_integers[el] -= damage
                if pirate_ship_integers[el] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_valid = False
                    break
    elif data[0] == "Repair":
        index = int(data[1])
        health = int(data[2])
        if 0 <= index < len(pirate_ship_integers):
            if pirate_ship_integers[index] + health > max_health:
                pirate_ship_integers[index] = max_health
            else:
                pirate_ship_integers[index] += health

    elif data[0] == "Status":
        count = 0
        for section in range(len(pirate_ship_integers)):
            if pirate_ship_integers[section] < max_health * 0.20:
                count += 1
        print(f"{count} sections need repair.")

    command = input()

if is_valid:
    print(f"Pirate ship status: {sum(pirate_ship_integers)}")
    print(f"Warship status: {sum(battle_ship_integers)}")
