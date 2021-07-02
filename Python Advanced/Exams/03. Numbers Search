from collections import deque


def numbers_searching(*args):
    numbers = deque(args)
    duplicates = []
    missing = []
    result = []
    while numbers:
        index = 0
        if numbers.count(numbers[index]) >= 2:
            duplicates.append(numbers[index])
            numbers.popleft()
        else:
            missing.append(numbers[index])
            numbers.popleft()

    miss_num = find_missing(sorted(missing))

    result.append(sorted(duplicates))
    result.insert(0, miss_num)
    return result


def find_missing(lst):
    return int("".join(str(el) for el in [x for x in range(lst[0], lst[-1] + 1)
            if x not in lst]))

