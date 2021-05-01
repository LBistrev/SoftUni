def even_or_odd(number):
    if number % 2 == 0:
        return True
    return False


number_as_string = input()
odd_sum = 0
even_sum = 0
for i in range(len(number_as_string)):
    num = int(number_as_string[i])
    if even_or_odd(num):
        even_sum += num
    else:
        odd_sum += num

print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
