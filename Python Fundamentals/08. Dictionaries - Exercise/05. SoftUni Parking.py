number_of_commands = int(input())
parking_validation = {}
for num in range(number_of_commands):
    command = input().split()
    if command[0] == "register":
        username = command[1]
        license_number = command[2]
        if username not in parking_validation:
            parking_validation[username] = license_number
            print(f"{username} registered {license_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_number}")
    elif command[0] == "unregister":
        username = command[1]
        if username not in parking_validation:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking_validation[username]

for user, number in parking_validation.items():
    print(f"{user} => {number}")
