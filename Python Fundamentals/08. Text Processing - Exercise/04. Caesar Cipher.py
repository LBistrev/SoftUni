text = input()
encrypted = ""
for char in text:
    new_letter = ord(char)
    new_letter += 3
    encrypted += chr(new_letter)

print(encrypted)
