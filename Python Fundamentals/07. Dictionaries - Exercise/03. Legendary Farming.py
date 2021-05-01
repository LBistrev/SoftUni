text = input()
possible_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
real_items = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials = {}
is_valid = False

while not is_valid:
    elements = text.split()
    for index in range(0, len(elements), 2):
        if is_valid:
            break
        quantity = int(elements[index])
        material = elements[index+1].lower()
        if material in real_items:
            real_items[material] += quantity
        else:
            if material not in junk_materials:
                junk_materials[material] = quantity
            else:
                junk_materials[material] += quantity
        for material, quantity in real_items.items():
            if quantity >= 250:
                print(f"{possible_items[material]} obtained!")
                real_items[material] -= 250
                is_valid = True
    if is_valid:
        break

    text = input()

sorted_real_items = sorted(real_items.items(), key=lambda kvp: (-kvp[1], kvp[0]))
for key, quantity in sorted_real_items:
    print(f"{key}: {quantity}")

sorted_junk_materials = sorted(junk_materials.items(), key=lambda kvp: kvp[0])
for key, quantity in sorted_junk_materials:
    print(f"{key}: {quantity}")
