first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
total_people_count = int(input())
count_hour = 0
sum_of_all_people_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency

while total_people_count > 0:
    count_hour += 1
    if count_hour % 4 == 0:
        continue
    if sum_of_all_people_per_hour >= total_people_count:
        break

    total_people_count -= sum_of_all_people_per_hour
print(f"Time needed: {count_hour}h.")
