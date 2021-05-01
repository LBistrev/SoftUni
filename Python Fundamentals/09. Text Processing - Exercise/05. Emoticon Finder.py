text = input()
symbol = ":"

result = []

for index in range(len(text)):
    if text[index] == symbol:
        result.append(f"{symbol}{text[index+1]}")
print("\n".join(result))
