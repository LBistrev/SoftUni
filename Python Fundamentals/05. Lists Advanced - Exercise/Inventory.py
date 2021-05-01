def is_item_exist(current_item, sequence_of_items):
    if current_item in sequence_of_items:
        return True
    return False


items = input().split(", ")
commands = input()

while not commands == "Craft!":
    data = commands.split(" - ")
    if data[0] == "Collect":
        item = data[1]
        if not is_item_exist(item, items):
            items.append(item)
    elif data[0] == "Drop":
        item = data[1]
        if is_item_exist(item, items):
            items.remove(item)
    elif data[0] == "Combine Items":
        old_item, new_item = data[1].split(":")
        if is_item_exist(old_item, items):
            index = items.index(old_item)
            items.insert(index+1, new_item)
    elif data[0] == "Renew":
        item = data[1]
        if is_item_exist(item, items):
            items.remove(item)
            items.append(item)

    commands = input()

print(", ".join(items))
