from itertools import permutations


def possible_permutations(seq):
    p_perms = permutations(seq)
    for p in p_perms:
        yield list(p)


[print(n) for n in possible_permutations([1, 2, 3])]
