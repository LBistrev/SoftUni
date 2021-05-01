text = input().strip()
result = {}

for char in text.strip():
    if char == " ":
        continue
    if char not in result:
        result[char] = 1
    else:
        result[char] += 1

for el in result.items():
    print(f"{el[0]} -> {el[1]}")
