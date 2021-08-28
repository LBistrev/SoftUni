def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_primes(sequence):
    primes = filter(lambda n: is_prime(n), sequence)
    for n in primes:
        yield n


# def is_prime(num):
#     return num > 1 and all(num % i for i in range(2, num))


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0, 4, 5, 6, 7, 123, 3553, 56453, 666, 704])))
