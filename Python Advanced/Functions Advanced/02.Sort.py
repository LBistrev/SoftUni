def sorted_nums(sequence_of_numbers):
    return sorted(sequence_of_numbers)


nums = [int(x) for x in input().split()]

print(sorted_nums(nums))