def reverse_array(left_idx, elements):
    if left_idx == len(elements) // 2:
        return
    right_idx = len(elements) - 1 - left_idx
    elements[left_idx], elements[right_idx] = elements[right_idx], elements[left_idx]
    reverse_array(left_idx + 1, elements)


elements = input().split()

reverse_array(0, elements)

print(' '.join(elements))

# elements = input().split()
# for left_index in range(len(elements) // 2):
#     right_index = len(elements) - 1 - left_index
#     elements[left_index], elements[right_index] = elements[right_index], elements[left_index]
#
# print(' '.join(elements))
