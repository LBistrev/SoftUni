def even_parameters(func):
    def wrapper(*args):
        try:
            for el in args:
                if not el % 2 == 0:
                    return "Please use only even numbers!"
        except TypeError:
            return "Please use only even numbers!"
        return func(*args)
    return wrapper