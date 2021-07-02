from collections import deque

def list_manipulator(sequence, *args):
    numbers = deque(sequence)
    if args[0] == "add" and args[1] == "beginning":
        nums = args[2:]
        for n in range(len(nums) - 1, -1, -1):
            numbers.appendleft(nums[n])
    elif args[0] == "add" and args[1] == "end":
        nums = args[2:]
        for n in range(len(nums)):
            numbers.append(nums[n])
    elif args[0] == "remove" and args[1] == "beginning":
        if len(args) <= 2:
            numbers.popleft()
        else:
            amount = args[2]
            if amount:
                for n in range(amount):
                    numbers.popleft()
    elif args[0] == "remove" and args[1] == "end":
        if len(args) <= 2:
            numbers.pop()
        else:
            amount = args[2]
            if amount:
                for n in range(amount):
                    numbers.pop()

    return list(numbers)



