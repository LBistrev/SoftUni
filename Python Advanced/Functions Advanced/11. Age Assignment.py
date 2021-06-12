def age_assignment(*args, **kwargs):
    people_dict = {name: 0 for name in args}
    for key, value in kwargs.items():
        for name in people_dict:
            if name.startswith(key):
                people_dict[name] = value
    return people_dict
