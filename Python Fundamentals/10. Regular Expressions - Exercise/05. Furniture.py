import re

data = input()
furnitures = []
total = 0
pattern = r">>(?P<furniture>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>(\d+))(\s|$)"
while not data == "Purchase":
    match = re.match(pattern, data)
    if match:
        valid_data = match.groupdict()
        furnitures.append(valid_data["furniture"])
        total += int(valid_data["quantity"]) * float(valid_data["price"])
    data = input()

print("Bought furniture:")
if furnitures:
    for furn in furnitures:
        print(furn)
print(f"Total money spend: {total:.2f}")
