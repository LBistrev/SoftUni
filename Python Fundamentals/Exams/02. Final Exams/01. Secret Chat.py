concealed_message = input()
commands = input()
while not commands == "Reveal":
    current_data = commands.split(":|:")
    if current_data[0] == "InsertSpace":
        index = int(current_data[1])
        concealed_message = list(concealed_message)
        concealed_message.insert(index, " ")
        concealed_message = "".join(concealed_message)
        print(concealed_message)
    elif current_data[0] == "Reverse":
        substring = current_data[1]
        if substring in concealed_message:
            reversed_substring = substring[::-1]
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message += reversed_substring
            print(concealed_message)
        else:
            print("error")

    elif current_data[0] == "ChangeAll":
        substring = current_data[1]
        replacement = current_data[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
    commands = input()

print(f"You have a new text message: {concealed_message}")
