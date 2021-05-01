import re
text = input()
pattern = r"(?<=(/|\=))[A-Z][a-zA-Z]{2,}(?=\1)"

valid = [obj.group() for obj in re.finditer(pattern, text)]
destinations = sum([len(place) for place in valid])
print(f"Destinations: {', '.join(valid)}")
print(f"Travel Points: {destinations}")
