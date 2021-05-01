def sum_numbers(n1, n2):
    result = n1 + n2
    return result


def subtract(n1, n2, n3):
    result = sum_numbers(number_1, number_2)
    return result - n3


def add_and_subtract(n1, n2, n3):
    return subtract(n1, n2, n3)


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
total = add_and_subtract(number_1, number_2, number_3)
print(total)
