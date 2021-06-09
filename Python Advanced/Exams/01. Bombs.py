from collections import deque

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings_stack = [int(x) for x in input().split(", ")]

DATURA_BOMBS = 40
CHERRY_BOMBS = 60
SMOKE_DECOY_BOMBS = 120
count_datura = 0
count_cherry = 0
count_smoke = 0
sum_bombs = 0
is_succeed = False
while len(bomb_effects) > 0 and len(bomb_casings_stack) > 0:
    if count_smoke >= 3 and count_cherry >= 3 and count_datura >= 3:
        is_succeed = True
        break
    index = 0
    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings_stack.pop()
    sum_bombs = current_effect + current_casing

    if sum_bombs == DATURA_BOMBS:
        count_datura += 1
    elif sum_bombs == CHERRY_BOMBS:
        count_cherry += 1
    elif sum_bombs == SMOKE_DECOY_BOMBS:
        count_smoke += 1
    else:
        if current_casing - 5 < 0:
            break
        else:
            bomb_effects.appendleft(current_effect)
            bomb_casings_stack.append(current_casing - 5)

if is_succeed:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if not bomb_effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
if not bomb_casings_stack:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings_stack])}")
print(f"Cherry Bombs: {count_cherry}")
print(f"Datura Bombs: {count_datura}")
print(f"Smoke Decoy Bombs: {count_smoke}")
