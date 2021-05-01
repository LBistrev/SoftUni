quantity = int(input())
day = int(input())
christmas_spirit = 0
money_spent = 0
ORNAMENT_SET = 2
TREE_SKIRT = 5
TREE_GARLANDS = 3
TREE_LIGHTS = 15

for days in range(1, day + 1):
    if days % 11 == 0:
        quantity += 2
    if days % 2 == 0:
        money_spent += quantity * ORNAMENT_SET
        christmas_spirit += 5
    if days % 3 == 0:
        money_spent += quantity * TREE_SKIRT + quantity * TREE_GARLANDS
        christmas_spirit += 13
    if days % 5 == 0:
        money_spent += quantity * TREE_LIGHTS
        christmas_spirit += 17
        if days % 3 == 0:
            christmas_spirit += 30
    if days % 10 == 0:
        christmas_spirit -= 20
        money_spent += TREE_SKIRT + TREE_GARLANDS + TREE_LIGHTS
    
    if days == day and days % 10 == 0:
        christmas_spirit -= 30

print(f"Total cost: {money_spent}")
print(f"Total spirit: {christmas_spirit}")
