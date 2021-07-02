from collections import deque


def stock_availability(inventory, *args):
    inventory = deque(inventory)
    command = args[0]
    if command == "delivery":
        for index in range(1, len(args)):
            inventory.append(args[index])
    if command == "sell":
        if len(args) >= 2:
            if isinstance(args[1], int):
                for i in range(args[1]):
                    if inventory:
                        inventory.popleft()
            elif isinstance(args[1], str):
                for index in range(1, len(args)):
                    while args[index] in inventory:
                        inventory.remove(args[index])
        else:
            inventory.popleft()

    return list(inventory)
