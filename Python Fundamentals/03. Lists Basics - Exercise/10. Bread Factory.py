working_day_events = input().split("|")
initial_energy = 100
initial_coins = 100
ingredient = ""
command_event = True
for each_round in working_day_events:
    event, value = each_round.split("-")
    value = int(value)
    if event == "rest":
        if initial_energy + value > 100:
            current_energy = 100 - initial_energy
        else:
            current_energy = value
        initial_energy += current_energy
        print(f"You gained {current_energy} energy.")
        print(f"Current energy: {initial_energy}.")

    elif event == "order":
        initial_energy -= 30
        if initial_energy >= 0:
            initial_coins += value
            print(f"You earned {value} coins.")
        else:
            initial_energy += 50 + 30
            print("You had to rest!")
    else:
        ingredient = event
        if initial_coins - value <= 0:
            print(f"Closed! Cannot afford {ingredient}.")
            command_event = False
            break
        else:
            initial_coins -= value
            print(f"You bought {ingredient}.")

if command_event:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")


