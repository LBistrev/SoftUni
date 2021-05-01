def is_number_perfect(num):
    proper_divisors = []

    for n in range(1, num):
        if num % n == 0:
            proper_divisors.append(n)
    if sum(proper_divisors) == num:
        return True
    return False


number = int(input())
if is_number_perfect(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
