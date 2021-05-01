import re

text = input()

pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-z]+-?[a-z]+(\.[a-z]+)+"

valid_emails = [email.group() for email in re.finditer(pattern, text)]

for mail in valid_emails:
    print(mail)
