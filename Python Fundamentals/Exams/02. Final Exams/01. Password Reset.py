text = input()
command = input()
while not command == "Done":
    data = command.split()
    if data[0] == "TakeOdd":
        text = [text[char] for char in range(1, len(text), 2)]
        text = "".join(text)
        print(text)
    elif data[0] == "Cut":
        index = int(data[1])
        length = int(data[2])
        to_remove = text[index:index+length]
        text = text.replace(to_remove, "", 1)
        print(text)
    elif data[0] == "Substitute":
        substring = data[1]
        substitute = data[2]
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)
        else:
            print("Nothing to replace!")
    command = input()
print(f"Your password is: {text}")
