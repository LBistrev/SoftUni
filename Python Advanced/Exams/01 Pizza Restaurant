from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
pizza_employees = [int(x) for x in input().split(", ")]

total_pizzas = 0
while pizza_orders and pizza_employees:
    first_order = pizza_orders.popleft()
    if first_order > 10 or first_order <= 0:
        continue
    last_employee = pizza_employees.pop()
    if first_order <= last_employee:
        total_pizzas += first_order
    if first_order > last_employee:
        first_order -= last_employee
        pizza_orders.appendleft(first_order)
        total_pizzas += last_employee

if not pizza_orders and pizza_employees:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join([str(x) for x in pizza_employees])}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")
