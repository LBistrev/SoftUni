neighborhood = [int(num) for num in input().split("@")]
commands = input()
index = 0
while not commands == "Love!":
    data = commands.split()
    length = int(data[1])
    index += length
    if 0 <= index < len(neighborhood):
        if neighborhood[index] == 0:
            print(f"Place {index} already had Valentine's day.")
        else:
            neighborhood[index] -= 2
            if neighborhood[index] <= 0:
                print(f"Place {index} has Valentine's day.")
    else:
        index = 0
        if 0 <= index < len(neighborhood):
            if neighborhood[index] == 0:
                print(f"Place {index} already had Valentine's day.")
            else:
                neighborhood[index] -= 2
                if neighborhood[index] <= 0:
                    print(f"Place {index} has Valentine's day.")
    commands = input()
print(f"Cupid's last position was {index}.")
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    neighborhood = [house for house in neighborhood if house != 0]
    print(f"Cupid has failed {len(neighborhood)} places.")
