command_data = input()
cities_dict = {}
while not command_data == "Sail":
    town, population, gold = command_data.split("||")
    if town not in cities_dict:
        cities_dict[town] = {"population": int(population), "gold": int(gold)}
    else:
        cities_dict[town]["population"] += int(population)
        cities_dict[town]["gold"] += int(gold)
    command_data = input()

events = input()
while not events == "End":
    current_event = events.split("=>")
    town = current_event[1]
    if current_event[0] == "Plunder":
        people = int(current_event[2])
        gold = int(current_event[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        cities_dict[town]["population"] -= people
        cities_dict[town]["gold"] -= gold
    if cities_dict[town]["population"] <= 0 or cities_dict[town]["gold"] <= 0:
        del cities_dict[town]
        print(f"{town} has been wiped off the map!")
    elif current_event[0] == "Prosper":
        gold = int(current_event[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities_dict[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities_dict[town]['gold']} gold.")

    events = input()
sorted_cities = sorted(cities_dict.items(), key=lambda kvp: (-kvp[1]["gold"], kvp))

if cities_dict:
    print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")
    for town, data in sorted_cities:
        print(f"{town} -> Population: {data['population']} citizens, Gold: {data['gold']} kg")

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
