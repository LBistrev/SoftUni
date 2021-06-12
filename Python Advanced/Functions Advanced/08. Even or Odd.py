def even_odd(*args):
    command = args[-1]
    numbers = args[:-1]
    if command == "even":
        numbers = list((filter(lambda n: n % 2 == 0, numbers)))

    elif command == "odd":
        numbers = list((filter(lambda n: n % 2 != 0, numbers)))

    return numbers