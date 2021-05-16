data = input()
contests_dict = {}
while not data == "end of contests":
    contest, password = data.split(":")
    if contest not in contests_dict:
        contests_dict[contest] = password
    data = input()

other_info = input()
users_dict = {}
submissions_dict = {}
while not other_info == "end of submissions":
    contest, password, username, points = other_info.split("=>")
    points = int(points)
    if contest in contests_dict:
        if contests_dict[contest] == password:
            if username not in users_dict:
                users_dict[username] = {}
                users_dict[username][contest] = points
            if contest not in users_dict[username]:
                users_dict[username][contest] = points
            else:
                if users_dict[username][contest] < points:
                    users_dict[username][contest] = points
    other_info = input()

sum_points = 0
for user, users_data in users_dict.items():
    for values in users_data.items():
        sum_points += values[1]
    submissions_dict[user] = sum_points
    sum_points = 0
best_student = sorted(submissions_dict.items(), key=lambda kvp: -kvp[1])
print(f"Best candidate is {best_student[0][0]} with total {best_student[0][1]} points.")
print("Ranking:")
sorted_users = dict(sorted(users_dict.items(), key=lambda kvp: kvp[0]))
for user, current_data in sorted_users.items():
    sorted_users[user] = dict(sorted(sorted_users[user].items(), key=lambda kvp: -kvp[1]))

for student, data in sorted_users.items():
    print(student)
    for contest, points in data.items():
        print(f"#  {contest} -> {points}")

