data = input()
courses = {}
while not data == "end":
    course_name, student_name = data.split(" : ")
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)
    data = input()

sorted_courses = sorted(courses.items(), key=lambda kvp: -len(kvp[1]))

for name, value in sorted_courses:
    print(f"{name}: {len(value)}")
    sorted_value = sorted(value)
    for student in sorted_value:
        print(f"-- {student}")
