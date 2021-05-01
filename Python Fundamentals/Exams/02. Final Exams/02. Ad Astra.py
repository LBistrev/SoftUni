import re
text = input()
sum_calories = 0
pattern = r"(#|\|)(?P<item>[a-zA-Z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>([0-9][0-9]{0,3}|10000))\1"

valid_items = [data.groupdict() for data in re.finditer(pattern, text)]
for object in valid_items:
    sum_calories += int(object["calories"])
days = sum_calories // 2000

print(f"You have food to last you for: {days} days!")
for data in valid_items:
    print(f"Item: {data['item']}, Best before: {data['date']}, Nutrition: {data['calories']}")
