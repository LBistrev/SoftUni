# def fibonacci():
#     f1 = 0
#     f2 = 1
#     yield f1
#     yield f2
#
#     fn_1 = f2
#     fn_2 = f1
#     while True:
#         fn = fn_1 + fn_2
#         yield fn
#         fn_2 = fn_1
#         fn_1 = fn
#

# generator = fibonacci()
# for i in range(5):
#     print(next(generator))


def fibonacci():
    i = 0
    while True:
        yield fib_n(i)
        i += 1


def fib_n(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_n(n-1) + fib_n(n-2)


generator = fibonacci()
for i in range(5):
    print(next(generator))
