sequence_of_numbers = input().split()

text = input()
new_text = ""
for numbers in sequence_of_numbers:
    index = 0
    for el in numbers:
        index += int(el)
    if index in range(len(text)):
        new_text += text[index]
        text = text.replace(text[index], "", 1)
    else:
        index -= len(text)
        for i in range(len(text)):
            if i == index:
                new_text += text[i]
                text = text.replace(text[i], "", 1)
                break

print(new_text)
