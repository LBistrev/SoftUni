neighborhood = [int(num) for num in input().split("@")]
command = input()
current_index = 0
while not command == "Love!":
    jump, index = command.split()
    index = int(index)
    current_index += index
    if current_index < len(neighborhood):
        if neighborhood[current_index] <= 0:
            print(f"Place {current_index} already had Valentine's day.")
        else:
            neighborhood[current_index] -= 2
            if neighborhood[current_index] <= 0:
                print(f"Place {current_index} has Valentine's day.")
    else:
        current_index = 0
        if neighborhood[current_index] <= 0:
            print(f"Place {current_index} already had Valentine's day.")
        else:
            neighborhood[current_index] -= 2
            if neighborhood[current_index] <= 0:
                print(f"Place {current_index} has Valentine's day.")

    command = input()
counter = 0
print(f"Cupid's last position was {current_index}.")
for house in neighborhood:
    if house > 0:
        counter += 1
if sum(neighborhood) == 0:
    print(f"Mission was successful.")
else:

    print(f"Cupid has failed {counter} places.")
