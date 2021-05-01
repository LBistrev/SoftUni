list_as_string = input().split("|")
count_rooms = 0
initial_health = 100
current_health = 0
initial_bitcoins = 0
current_bitcoins = 0
for room in list_as_string:
    command, number = room.split()
    current_health = int(number)

    if command == "potion":
        count_rooms += 1
        if initial_health < 100:
            initial_health += current_health
            if initial_health > 100:
                current_health = abs(initial_health - current_health - 100)
                initial_health = 100
            print(f"You healed for {current_health} hp.")
            print(f"Current health: {initial_health} hp.")

    elif command == "chest":
        count_rooms += 1
        current_bitcoins = int(number)
        initial_bitcoins += int(number)

        print(f"You found {current_bitcoins} bitcoins.")
    else:
        count_rooms += 1
        monster = command
        attack = int(number)
        initial_health -= attack
        current_health = initial_health
        if initial_health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {count_rooms}")
            break
if initial_health > 0:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")
