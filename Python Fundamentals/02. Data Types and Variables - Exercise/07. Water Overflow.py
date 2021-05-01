CAPACITY = 255
number = int(input())
liters_count = 0
for n in range(number):
    liters = int(input())
    if liters > CAPACITY:
        print("Insufficient capacity!")
    else:
        liters_count += liters
        if liters_count > CAPACITY:
            print("Insufficient capacity!")
            liters_count -= liters
            continue
print(liters_count)
