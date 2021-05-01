import re

text = input()
word = input()

pattern = rf"\b{word}\b"
words = re.findall(pattern, text, re.IGNORECASE)
print(len(words))
