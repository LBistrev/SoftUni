def even_or_odd(nums):
    result = 0
    if command == "Odd":
        result = sum([num for num in numbers if num % 2 != 0])

    elif command == "Even":
        result = sum([num for num in numbers if num % 2 == 0])

    return result * len(nums)


command = input()
numbers = [int(x) for x in input().split()]
print(even_or_odd(numbers))