def best_list_pureness(*args):
    list_nums, k = args
    total_score = 0
    max_score = 0
    count_rotations = 0
    for index_rotate in range(k + 1):

        for index_list in range(len(list_nums)):

            total_score += list_nums[index_list] * index_list
        if max_score < total_score:
            max_score = total_score
            count_rotations = index_rotate
        current_el = list_nums.pop()
        list_nums.insert(0, current_el)
        total_score = 0

    return f"Best pureness {max_score} after {count_rotations} rotations"
