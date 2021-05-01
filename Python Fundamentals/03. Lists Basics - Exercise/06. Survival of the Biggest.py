list_of_integer = input().split()
numbers_to_remove = int(input())

list_of_biggest = []

for numbers in list_of_integer:
    number = int(numbers)
    list_of_biggest.append(number)

for smallest in range(numbers_to_remove):
    min_number = min(list_of_biggest)
    list_of_biggest.remove(min_number)

print(list_of_biggest)
