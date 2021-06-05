n = int(input())
names = set()
sum_numbers = 0
sequence_of_odd = set()
sequence_of_even = set()
result = 0
for row in range(1, n + 1):
    name = input()
    for char in name:
        sum_numbers += ord(char)
    result = sum_numbers // row
    if result % 2 == 0:
        sequence_of_even.add(result)
    else:
        sequence_of_odd.add(result)
    sum_numbers = 0
sum_odd = sum(sequence_of_odd)
sum_even = sum(sequence_of_even)

if sum_odd == sum_even:
    print(', '.join([str(el) for el in list(sequence_of_odd.union(sequence_of_even))]))
elif sum_odd > sum_even:
    print(', '.join([str(el) for el in list(sequence_of_odd.difference(sequence_of_even))]))
elif sum_even > sum_odd:
    print(', '.join([str(el) for el in list(sequence_of_even.symmetric_difference(sequence_of_odd))]))

