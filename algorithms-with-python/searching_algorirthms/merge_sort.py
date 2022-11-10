# print(*(sorted([int(x) for x in input().split()])), sep=' ')

def merge_arrays(left_half, right_half):
    result = [None] * (len(left_half) + len(right_half))
    left_idx = 0
    right_idx = 0
    result_idx = 0

    while left_idx < len(left_half) and right_idx < len(right_half):
        if left_half[left_idx] < right_half[right_idx]:
            result[result_idx] = left_half[left_idx]
            left_idx += 1
        else:
            result[result_idx] = right_half[right_idx]
            right_idx += 1
        result_idx += 1

    while left_idx < len(left_half):
        result[result_idx] = left_half[left_idx]
        left_idx += 1
        result_idx += 1

    while result_idx < len(right_half):
        result[result_idx] = right_half[right_idx]
        right_idx += 1
        result_idx += 1

    return result


def merge_sort(nums):
    if len(nums) == 1:
        return nums

    mid_idx = len(nums) // 2
    left_half = nums[:mid_idx]
    right_half = nums[mid_idx:]

    return merge_arrays(merge_sort(left_half), merge_sort(right_half))


nums = [int(x) for x in input().split()]
result = merge_sort(nums)
print(*result, sep=' ')
