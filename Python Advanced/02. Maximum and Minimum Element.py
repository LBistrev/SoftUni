number = int(input())
stack = []
for i in range(number):
    data = input().split()
    if data[0] == "1":
        stack.append(int(data[1]))
    elif data[0] == "2":
        if stack:
            stack.pop()
    elif data[0] == "3":
        if stack:
            print(max(stack))
    elif data[0] == "4":
        if stack:
            print(min(stack))
result = []
while stack:
    result.append(stack.pop())

print(", ".join([str(num) for num in result]))
