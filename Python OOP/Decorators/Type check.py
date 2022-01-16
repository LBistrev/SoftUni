def type_check(type_el):
    def decorator(func):
        def wrapper(n):
            if type(n) == type_el:
                return func(n)
            return "Bad Type"

        return wrapper

    return decorator