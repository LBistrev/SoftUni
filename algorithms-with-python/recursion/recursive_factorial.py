def calc_factorial(number):
    if number == 0:
        return 1
    return number * calc_factorial(number - 1)


number = int(input())
print(calc_factorial(number))
