number_of_cars = int(input())
cars = {}
for num in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    cars[car] = {"mileage": mileage, "fuel": fuel}

commands = input()
while not commands == "Stop":
    data = commands.split(" : ")
    if data[0] == "Drive":
        car = data[1]
        distance = int(data[2])
        fuel = int(data[3])
        if not fuel <= cars[car]["fuel"]:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["mileage"] += distance
            cars[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]["mileage"] >= 100000:
                print(f"Time to sell the {car}!")
                del cars[car]
    elif data[0] == "Refuel":
        car = data[1]
        fuel = int(data[2])
        max_fuel = 75
        if cars[car]["fuel"] + fuel > max_fuel:
            print(f"{car} refueled with {max_fuel - cars[car]['fuel']} liters")
            cars[car]["fuel"] += max_fuel - cars[car]['fuel']
        else:
            print(f"{car} refueled with {fuel} liters")
            cars[car]["fuel"] += fuel
    elif data[0] == "Revert":
        car = data[1]
        kilometers = int(data[2])
        cars[car]["mileage"] -= kilometers
        if cars[car]["mileage"] < 10000:
            cars[car]["mileage"] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    commands = input()

sorted_cars = sorted(cars.items(), key=lambda kvp: (-kvp[1]["mileage"], kvp[0]))
if sorted_cars:
    for car, data in sorted_cars:
        print(f"{car} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")
