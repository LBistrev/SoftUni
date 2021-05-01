numbers_as_string = input().split()
number_descending = sorted(numbers_as_string, reverse=True)
print("".join(number_descending))
