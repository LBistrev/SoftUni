from collections import deque


def is_empty_list(sequence):
    if sequence:
        return True
    return False


customers_queues = deque([int(el) for el in input().split(", ")])
taxis_times_as_stack = [int(el) for el in input().split(", ")]

total_time = 0

while len(customers_queues):
    if not taxis_times_as_stack:
        break
    index = 0
    if is_empty_list(taxis_times_as_stack):
        last_taxi = taxis_times_as_stack.pop()
        if customers_queues[index] <= last_taxi:
            total_time += customers_queues[index]
            current_customer = customers_queues.popleft()


if customers_queues:
    print(f"Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(el) for el in customers_queues])}")
else:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
