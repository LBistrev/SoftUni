def even_numbers(num):
    return num % 2 == 0


numbers = [int(x) for x in input().split()]

print(list(filter(even_numbers, numbers)))