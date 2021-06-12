def func_executor(*args):
    result = []

    for function, nums in args:
        result.append(function(*nums))

    return result