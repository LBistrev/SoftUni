substrings = input().split(", ")
text = input().split(", ")
result = []
for string in substrings:
    for char in text:
        if string in char:
            if string not in result:
                result.append(string)

print(result)
