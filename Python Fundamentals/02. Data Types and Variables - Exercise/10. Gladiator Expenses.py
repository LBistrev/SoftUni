lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
trashed_helmet = 0
trashed_sword = 0
trashed_shield = 0
trashed_armor = 0
counter_shield = 0
for lost in range(1, lost_fights_count + 1):

    if lost % 2 == 0:
        trashed_helmet += helmet_price
    if lost % 3 == 0:
        trashed_sword += sword_price
    if lost % 2 == 0 and lost % 3 == 0:
        trashed_shield += shield_price
        counter_shield += 1
    if counter_shield == 2:
        trashed_armor += armor_price
        counter_shield = 0
total_costs = trashed_helmet + trashed_sword + trashed_shield + trashed_armor
print(f"Gladiator expenses: {total_costs:.2f} aureus")
