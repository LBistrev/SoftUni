sums_of_each_beggar_as_string = input().split(", ")
number_of_beggars = int(input())
sum_of_each_beggar = []
start_index = 0
for beggar in range(1, number_of_beggars + 1):
    current_sum = 0
    for index in range(start_index, len(sums_of_each_beggar_as_string), number_of_beggars):
        current_sum += int(sums_of_each_beggar_as_string[index])
    sum_of_each_beggar.append(current_sum)
    start_index += 1
print(sum_of_each_beggar)
