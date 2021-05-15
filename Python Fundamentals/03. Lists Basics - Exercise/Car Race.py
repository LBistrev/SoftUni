numbers = input().split()
center = len(numbers) // 2
left_side = numbers[:center]
right_side = numbers[center+1:]
reversed_right_side = right_side[::-1]
time_left_side = 0
time_right_side = 0
for left in left_side:
    num = int(left)
    if num == 0:
        time_left_side -= time_left_side * 0.20
    else:
        time_left_side += num

for right in reversed_right_side:
    num1 = int(right)
    if num1 == 0:
        time_right_side -= time_right_side * 0.20
    else:
        time_right_side += num1
if time_right_side < time_left_side:
    print(f"The winner is right with total time: {time_right_side:.1f}")
else:
    print(f"The winner is left with total time: {time_left_side:.1f}")
