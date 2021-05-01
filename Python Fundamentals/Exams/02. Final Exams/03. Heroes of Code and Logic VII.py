number_of_heroes = int(input())
heroes_dict = {}
for num in range(number_of_heroes):
    hero_name, hit_points, mana_points = input().split()
    hit_points = int(hit_points)
    mana_points = int(mana_points)
    if hero_name not in heroes_dict:
        heroes_dict[hero_name] = {}
        heroes_dict[hero_name] = {"HP": hit_points, "MP": mana_points}

commands = input()
while not commands == "End":
    current_data = commands.split(" - ")
    if current_data[0] == "CastSpell":
        hero_name = current_data[1]
        mana_points_needed = int(current_data[2])
        spell_name = current_data[3]
        if heroes_dict[hero_name]["MP"] >= mana_points_needed:
            heroes_dict[hero_name]["MP"] -= mana_points_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif current_data[0] == "TakeDamage":
        hero_name = current_data[1]
        damage = int(current_data[2])
        attacker = current_data[3]
        heroes_dict[hero_name]["HP"] -= damage
        if heroes_dict[hero_name]["HP"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name]['HP']} HP left!")
        else:
            del heroes_dict[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
    elif current_data[0] == "Recharge":
        hero_name = current_data[1]
        amount = int(current_data[2])

        if heroes_dict[hero_name]["MP"] + amount > 200:
            print(f"{hero_name} recharged for {200 - heroes_dict[hero_name]['MP']} MP!")
            heroes_dict[hero_name]["MP"] = 200
        else:
            heroes_dict[hero_name]["MP"] += amount
            print(f"{hero_name} recharged for {amount} MP!")
    elif current_data[0] == "Heal":
        hero_name = current_data[1]
        amount = int(current_data[2])

        if heroes_dict[hero_name]["HP"] + amount > 100:
            print(f"{hero_name} healed for {100 - heroes_dict[hero_name]['HP']} HP!")
            heroes_dict[hero_name]["HP"] = 100
        else:
            heroes_dict[hero_name]["HP"] += amount
            print(f"{hero_name} healed for {amount} HP!")
    commands = input()

sorted_heroes = sorted(heroes_dict.items(), key=lambda kvp: (-kvp[1]["HP"], kvp[0]))
if sorted_heroes:
    for hero, data in sorted_heroes:
        print(hero)
        for value in data:
            print(f"  {value}: {data[value]}")
