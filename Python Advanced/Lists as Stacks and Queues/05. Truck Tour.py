# from collections import deque
#
# petrol_pumps = int(input())
# pumps = deque()
#
# for i in range(petrol_pumps):
#     pump = [int(x) for x in input().split()]
#     pumps.append(pump)
#
# for index in range(petrol_pumps):
#     is_valid = True
#     fuel = 0
#
#     for _ in range(petrol_pumps):
#         current = pumps.popleft()
#         fuel += current[0] - current[1]
#         if fuel < 0:
#             is_valid = False
#         pumps.append(current)
#
#     if is_valid:
#         print(index)
#         break
#     pumps.append(pumps.popleft())
from collections import deque
number_of_petrol_pumps = int(input())
pumps = deque()
for _ in range(number_of_petrol_pumps):
    pumps.append([int(x) for x in input().split()])
petrol_pumps_indexes = []
for index in range(number_of_petrol_pumps):
    fuel_tank = 0
    travelled = 0
    for data in pumps:
        fuel, distance = data[0], data[1]
        fuel_tank += fuel
        if fuel_tank < distance:
            break

        travelled += 1
        fuel_tank -= distance
    if travelled == len(pumps):
        print(index)

        break
    pumps.rotate(-1)



