commands = input()
results = {}
submissions = {}
while not commands == "exam finished":
    if "banned" in commands:
        username, disc = commands.split("-")
        results.pop(username)
    else:
        username, language, points = commands.split("-")
        points = int(points)
        if username not in results:
            results[username] = []
        results[username].append(points)
        if language not in submissions:
            submissions[language] = 1
        else:
            submissions[language] += 1

    commands = input()
max_grades = {}
for name, grade in results.items():
    max_grades[name] = max(grade)
sorted_students = sorted(max_grades.items(), key=lambda kvp: (-kvp[1], kvp[0]))
print("Results:")
for student, points in sorted_students:
    print(f"{student} | {points}")
print("Submissions:")
sorted_submissions = sorted(submissions.items(), key=lambda kvp: (-kvp[1], kvp[0]))
for language, sub in sorted_submissions:
    print(f"{language} - {sub}")
