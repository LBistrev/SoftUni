def is_water_enough(val, water):
    if val <= water:
        return True
    return False


fire_numbers = input().split("#")
amount_of_water = int(input())
cells = []
effort = 0
for fire in fire_numbers:
    type_fire, value = fire.split(" = ")
    value = int(value)
    if type_fire == "High":
        if 81 <= value <= 125:
            if is_water_enough(value, amount_of_water):
                amount_of_water -= value
                cells.append(value)
                effort += value * 0.25
    elif type_fire == "Low":
        if 1 <= value <= 50:
            if is_water_enough(value, amount_of_water):
                amount_of_water -= value
                cells.append(value)
                effort += value * 0.25
    elif type_fire == "Medium":
        if 51 <= value <= 80:
            if is_water_enough(value, amount_of_water):
                amount_of_water -= value
                cells.append(value)
                effort += value * 0.25

total_fire = sum(cells)
print("Cells:")
for cell in cells:
    print(f"- {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
