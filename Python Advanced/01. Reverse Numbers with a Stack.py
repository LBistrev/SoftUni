numbers = [int(num) for num in input().split()]

stack = []
while numbers:
    current_num = numbers.pop()
    stack.append(current_num)

print(" ".join([str(el) for el in stack]))
