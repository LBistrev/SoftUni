# # 1 Zad
# stack = []
# numbers_as_string = input().split()
# while numbers_as_string:
#     stack.append(numbers_as_string.pop())
#
# print(" ".join(stack))
# def is_valid(elements):
#     if len(elements) > 0:
#         return True
#     return False
#
# 2 Zadacha
# number = int(input())
# stack = []
#
# for val in range(number):
#     command = input().split()
#     if command[0] == "1":
#         stack.append(int(command[1]))
#     elif command[0] == "2":
#         if is_valid(stack):
#             stack.pop()
#     elif command[0] == "3":
#         if is_valid(stack):
#             print(max(stack))
#     elif command[0] == "4":
#         if is_valid(stack):
#             print(min(stack))
# reversed_numbers = []
# while stack:
#     reversed_numbers.append(str(stack.pop()))
# print(", ".join(reversed_numbers))

# 3 zadacha
# from collections import deque
#
# food_quantity = int(input())
#
# orders = deque()
#
# for order in input().split():
#     order = int(order)
#     orders.append(order)
# if orders:
#     print(max(orders))
# for i in range(len(orders)):
#     order = orders.popleft()
#     if order <= food_quantity:
#         food_quantity -= food_quantity - order
#     else:
#         break
#
# if len(orders) == 0:
#     print("Orders complete")
# else:
#     print(f"Orders left: {''.join([str(el) for el in orders])}")

# 4 Zadacha
# numbers = [int(num) for num in input().split()]
# rack_capacity = int(input())
#
# stack = []
# number_of_racks = 0
# current_rack_weight = 0
# while len(numbers):
#     current = numbers.pop()
#     if current + current_rack_weight > rack_capacity:
#         number_of_racks += 1
#         current_rack_weight = 0
#     number_of_racks += current
#
# print(number_of_racks)

# 5 Zadacha
# from collections import  deque
# queue = deque()
# number = int(input())
#
# for i in range(number):
#     pumps = input().split()
#     queue.append([int(pumps[0]), int(pumps[1])])
#
# for _ in range(number):
#     # can we make a circle
#     fuel_tank = 0
#     current_index = 0
#     for gas_pump in queue:
#         fuel, distance = gas_pump[0], gas_pump[1]
#         fuel_tank += fuel
#         if fuel_tank < distance:
#             break
#         fuel_tank -= distance
#         current_index += 1
#     if current_index == len(queue):
#         print(_)
#         break
#     queue.rotate(-1)

# 6 Zadacha

# expression = input()
# stack = []
# balanced = True
# for el in expression:
#     if el in "[{(":
#         stack.append(el)
#     elif el in "]})":
#         open = stack.pop()
#
#     if f"{open}{el}" not in ['[]', '{}', '()']:
#         balanced = False

# from collections import deque
#
# parentheses = deque(list(input()))
# balanced = []
#
# while parentheses:
#     balanced.append(parentheses.popleft())
#     if len(balanced) > 1:
#         if balanced[-2:] == ['(', ')'] \
#                 or balanced[-2:] == ['[', ']'] \
#                 or balanced[-2:] == ['{', '}']:
#             balanced.pop()
#             balanced.pop()
#
# if balanced:
#     print("NO")
# else:
#     print("YES")

