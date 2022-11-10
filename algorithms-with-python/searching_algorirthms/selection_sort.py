# nums = [int(x) for x in input().split()]
#
# for idx in range(len(nums)):
#     min_number = nums[idx]
#     min_idx = idx
#     for next_idx in range(idx + 1, len(nums)):
#         next_number = nums[next_idx]
#         if next_number < min_number:
#             min_number = next_number
#             min_idx = next_idx
#
#     nums[idx], nums[min_idx] = nums[min_idx], nums[idx]
#
# print(*nums, sep=" ")


for num in range(1, 100):
    if num // 3 == 0:
        print('A')
    if num // 5 == 0:
        print('B')
    if num // 15 == 0:
        print('AB')
