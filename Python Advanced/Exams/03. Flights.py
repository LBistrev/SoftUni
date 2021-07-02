def flights(*args):
    data = list(args)
    flights_dict = {}
    while not data[0] == "Finish":
        destination = data.pop(0)
        passengers = data.pop(0)
        if destination not in flights_dict:
            flights_dict[destination] = passengers
        else:
            flights_dict[destination] += passengers

    return flights_dict
