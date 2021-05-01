encrypted_message = input()

instructions = input()
while not instructions == "Decode":
    data = instructions.split("|")
    if data[0] == "Move":
        number_of_letters = int(data[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]
    elif data[0] == "Insert":
        index = int(data[1])
        value = data[2]
        encrypted_message = list(encrypted_message)
        encrypted_message.insert(index, value)
        encrypted_message = "".join(encrypted_message)
    elif data[0] == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
    instructions = input()

print(f"The decrypted message is: {encrypted_message}")
