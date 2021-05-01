single_text_as_string = input().split(", ")
command = input()
while not command == "Craft!":
    word, item = command.split(" - ")
    if word == "Collect":
        if item not in single_text_as_string:
            single_text_as_string.append(item)
    elif word == "Drop":
        if item in single_text_as_string:
            single_text_as_string.remove(item)
    elif word == "Combine Items":
        old_item, new_item  = item.split(":")
        if old_item in single_text_as_string:
            index_old_item = single_text_as_string.index(old_item)
            single_text_as_string.insert(index_old_item+1, new_item)
    elif word == "Renew":
        if item in single_text_as_string:
            single_text_as_string.remove(item)
            single_text_as_string.append(item)

    command = input()

print(f"{', '.join(single_text_as_string)}")
