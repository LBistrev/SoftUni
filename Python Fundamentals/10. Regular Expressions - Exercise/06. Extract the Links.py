import re
text = input()
websites = []
pattern = r"w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+"
while text:
    valid_web = [obj.group() for obj in re.finditer(pattern, text)]
    if valid_web:
        websites.extend(valid_web)
    text = input()
print(*websites, sep="\n")
