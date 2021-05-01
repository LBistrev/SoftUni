def loading_bar(num):
    load = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    if num == 0:
        return load
    current_num = int(num / 10)
    for index in range(current_num):
        load[index] = "%"
    return load


number = int(input())
result = loading_bar(number)
if result.count("%") == 10:
    print("100% Complete!")
    print(f"[{''.join(result)}]")
else:
    print(f"{number}% [{''.join(result)}]")
    print("Still loading...")
