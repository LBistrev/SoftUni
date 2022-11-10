def binary_search(nums, searched_num):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_el = nums[mid_idx]

        if mid_el == searched_num:
            return mid_idx

        if searched_num > mid_el:
            left = mid_idx + 1
        else:
            right = mid_idx - 1
    return -1


numbers = [int(x) for x in input().split()]
target = int(input())

print(binary_search(numbers, target))
