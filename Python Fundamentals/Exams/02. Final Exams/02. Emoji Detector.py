import re

text = input()
pattern_emoji = r"(::|\*\*)([A-Z][a-z]{2,})\1"
# pattern = r">>(?P<furniture>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>(\d+))(\s|$)"
pattern_numbers = r"\d"
cool_threshold_sum = 1
threshold = [int(num) for num in re.findall(pattern_numbers, text)]
coolest_emojis = []
for n in threshold:
    cool_threshold_sum *= n
print(f"Cool threshold: {cool_threshold_sum}")
emojis = [em.group() for em in re.finditer(pattern_emoji, text)]
end_emoji = []
for joji in emojis:
    sum_em = 0
    for char in joji:
        if char == ":" or char == "*":
            continue
        sum_em += ord(char)
    if sum_em >= cool_threshold_sum:
        coolest_emojis.append(joji)
if emojis:
    print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for emoji in coolest_emojis:
    print(emoji)
