destinations = input()
commands = input()
while not commands == "Travel":
    data = commands.split(":")
    if data[0] == "Add Stop":
        index = int(data[1])
        string = data[2]
        if 0 <= index < len(destinations):
            destinations = destinations[:index] + string + destinations[index:]
    elif data[0] == "Remove Stop":
        start_index = int(data[1])
        end_index = int(data[2])
        if 0 <= start_index < len(destinations) and 0 <= end_index < len(destinations):
            start = destinations[:start_index]
            end = destinations[end_index+1:]
            destinations = start + end
    elif data[0] == "Switch":
        old_string = data[1]
        new_string = data[2]
        if old_string in destinations:
            destinations = destinations.replace(old_string, new_string)
    print(destinations)
    commands = input()
print(f"Ready for world tour! Planned stops: {destinations}")
