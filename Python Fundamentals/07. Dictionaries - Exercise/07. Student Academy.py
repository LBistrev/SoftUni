rows = int(input())
students_dict = {}
for num in range(rows):
    student_name = input()
    grade = float(input())
    if student_name not in students_dict:
        students_dict[student_name] = []
    students_dict[student_name].append(grade)

higher_students = {}
for name, avg in students_dict.items():
    if sum(avg) / len(avg) >= 4.50:
        average = sum(avg) / len(avg)
        higher_students[name] = average

sorted_students = sorted(higher_students.items(), key=lambda kvp: -kvp[1])
for name, grade in sorted_students:
    print(f"{name} -> {grade:.2f}")
