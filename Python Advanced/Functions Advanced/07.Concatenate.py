def concatenate(*args):
    sequence = ""
    for el in args:
        sequence += el
    return sequence


print(concatenate("Soft", "Uni", "Is", "Great", "!"))