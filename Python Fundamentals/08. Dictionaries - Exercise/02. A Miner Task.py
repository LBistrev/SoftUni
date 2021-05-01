item = input()
result = {}
while not item == "stop":
    value = int(input())
    if item not in result:
        result[item] = value
    else:
        result[item] += value
    item = input()


for el in result.items():
    print(f"{el[0]} -> {el[1]}")
