def factorial(num1, num2):
    first_num = num1
    second_num = num2
    for first in range(num1 - 1, 0, -1):
        first_num *= first
    for second in range(num2 - 1, 0, -1):
        second_num *= second
    return first_num / second_num


number_1 = int(input())
number_2 = int(input())
result = factorial(number_1, number_2)
print(f"{result:.2f}")
