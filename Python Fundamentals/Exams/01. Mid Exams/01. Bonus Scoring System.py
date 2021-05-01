count_of_students = int(input())
count_of_lectors = int(input())
bonus = int(input())
count_attendances = []
list_of_students = []
result = 0
max_attendance = 0
for student in range(1, count_of_students + 1):
    attendances = int(input())
    count_attendances.append(attendances)
    total_bonus = (attendances / count_of_lectors * (5 + bonus))
    max_attendance = max(count_attendances)
    list_of_students.append(total_bonus)
    result = max(list_of_students)

print(f"Max Bonus: {round(result)}.")
print(f"The student has attended {max_attendance} lectures.")
