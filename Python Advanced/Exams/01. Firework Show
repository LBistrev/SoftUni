from collections import deque


def is_sum_of_nums_divided_by_3(num1, num2):
    if (num1 + num2) % 3 == 0 and not (num1 + num2) % 5 == 0:
        return True
    return False


def is_sum_of_nums_divided_by_5(num1, num2):
    if (num1 + num2) % 5 == 0 and not (num1 + num2) % 3 == 0:
        return True
    return False


def is_sum_of_nums_divided_by_5_and_3(num1, num2):
    if (num1 + num2) % 5 == 0 and (num1 + num2) % 3 == 0:
        return True
    return False


def is_show(num1, num2, num3):
    if num1 >= 3 and num2 >= 3 and num3 >= 3:
        return True
    return False


firework_effects_as_queue = deque([int(x) for x in input().split(", ")])
explosive_power_as_stack = [int(x) for x in input().split(", ")]

palm_firework = 0
willow_firework = 0
crossette_firework = 0

while firework_effects_as_queue and explosive_power_as_stack:
    if is_show(palm_firework, willow_firework, crossette_firework):
        break
    if firework_effects_as_queue[0] <= 0:
        firework_effects_as_queue.popleft()
        continue
    elif explosive_power_as_stack[-1] <= 0:
        explosive_power_as_stack.pop()
        continue
    else:
        current_firework_effect = firework_effects_as_queue.popleft()
        current_power = explosive_power_as_stack.pop()

        if is_sum_of_nums_divided_by_5_and_3(current_firework_effect, current_power):
            crossette_firework += 1
            continue

        if is_sum_of_nums_divided_by_3(current_firework_effect, current_power):
            palm_firework += 1
            continue
        elif is_sum_of_nums_divided_by_5(current_firework_effect, current_power):
            willow_firework += 1
            continue
        else:
            current_firework_effect -= 1
            firework_effects_as_queue.append(current_firework_effect)
            explosive_power_as_stack.append(current_power)

if is_show(palm_firework, willow_firework, crossette_firework):
    print("Congrats! You made the perfect firework show!")

else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects_as_queue:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects_as_queue])}")
if explosive_power_as_stack:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power_as_stack])}")

print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crossette_firework}")
