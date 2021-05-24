from collections import deque

food_quantity = int(input())

orders = deque((int(x) for x in input().split()))
stack = []
is_valid = True
if orders:
    print(max(orders))
while orders:
    index = 0
    if orders[index] <= food_quantity:
        food_quantity -= orders[index]
        stack.append(orders[index])
        orders.popleft()
    else:
        is_valid = False
        break
if is_valid:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")

