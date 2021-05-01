first, second = input().split()
result = 0

if len(first) >= len(second):
    for index in range(len(first)):
        if index < len(second):
            result += ord(first[index]) * ord(second[index])
        else:
            result += ord(first[index])
else:
    for index in range(len(second)):
        if index < len(first):
            result += ord(second[index]) * ord(first[index])
        else:
            result += ord(second[index])
print(result)
