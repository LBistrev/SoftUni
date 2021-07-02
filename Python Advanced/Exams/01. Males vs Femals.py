from collections import deque

males_as_stack = deque([int(x) for x in input().split()])
females_queue = deque([int(x) for x in input().split()])
matches = 0
while females_queue and males_as_stack:
    if females_queue[0] <= 0:
        first_female = females_queue.popleft()
    elif males_as_stack[-1] <= 0:
        last_male = males_as_stack.pop()
    elif females_queue[0] % 25 == 0:
        for _ in range(1):
            females_queue.popleft()
    elif males_as_stack[-1] % 25 == 0:
        for _ in range(1):
            males_as_stack.pop()
    else:
        first_female = females_queue.popleft()
        last_male = males_as_stack.pop()
        if first_female == last_male:
            matches += 1
        else:
            males_as_stack.append(last_male-2)


print(f"Matches: {matches}")
if males_as_stack:
    print(f"Males left: {', '.join([str(x) for x in reversed(males_as_stack)])}")
else:
    print("Males left: none")
if females_queue:
    print(f"Females left: {', '.join(str(x) for x in females_queue)}")
else:
    print("Females left: none")
