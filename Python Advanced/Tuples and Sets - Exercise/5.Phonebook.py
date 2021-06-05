data = input()

phonebook = {}
while not data.isdigit():
    name, number = data.split("-")
    if name not in phonebook:
        phonebook[name] = number
    data = input()

for _ in range(int(data)):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
