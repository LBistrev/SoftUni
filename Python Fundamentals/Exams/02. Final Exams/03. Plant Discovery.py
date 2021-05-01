number = int(input())
plants_dict = {}
for num in range(number):
    plant, rarity = input().split("<->")
    rarity = int(rarity)
    plants_dict[plant] = {"rarity": rarity, "rating": []}

command = input()
while not command == "Exhibition":
    data = command.split()
    if data[0] == "Rate:":
        plant = data[1]
        rating = int(data[3])
        if plant in plants_dict:
            plants_dict[plant]["rating"].append(rating)
        else:
            print("error")
    elif data[0] == "Update:":
        plant = data[1]
        new_rarity = int(data[3])
        if plant in plants_dict:
            plants_dict[plant]["rarity"] = new_rarity
        else:
            print("error")
    elif data[0] == "Reset:":
        plant = data[1]
        if plant in plants_dict:
            plants_dict[plant]["rating"].clear()
        else:
            print("error")
    else:
        print("error")
    command = input()

for plant, value in plants_dict.items():
    if value["rating"]:
        avg = sum(value["rating"]) / len(value["rating"])
    else:
        avg = 0
    plants_dict[plant]["avg"] = avg

sorted_plants = sorted(plants_dict.items(), key=lambda kvp: (-kvp[1]["rarity"], -kvp[1]["avg"]))

print("Plants for the exhibition:")
if sorted_plants:
    for plant_name, average_rating in sorted_plants:
        print(f"- {plant_name}; Rarity: {average_rating['rarity']}; Rating: {average_rating['avg']:.2f}")
