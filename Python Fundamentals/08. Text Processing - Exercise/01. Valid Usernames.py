characters = input().split(", ")

for username in characters:
    if 3 <= len(username) <= 16:
        if username.isalnum() or "-" in username or "_" in username:
            print(username)
