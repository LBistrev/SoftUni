def piece_in_collection(text, collection):
    if text in collection:
        return True
    return False


number_of_pieces = int(input())
pieces_dict = {}
for num in range(number_of_pieces):
    pieces, composer, key = input().split("|")
    pieces_dict[pieces] = {"composer": composer, "key": key}

command = input()
while not command == "Stop":
    data = command.split("|")
    if data[0] == "Add":
        piece = data[1]
        composer = data[2]
        key = data[3]
        if piece_in_collection(piece, pieces_dict):
            print(f"{piece} is already in the collection!")
        else:
            pieces_dict[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif data[0] == "Remove":
        piece = data[1]
        if piece_in_collection(piece, pieces_dict):
            del pieces_dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif data[0] == "ChangeKey":
        piece = data[1]
        new_key = data[2]
        if piece_in_collection(piece, pieces_dict):
            pieces_dict[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

sorted_pieces = sorted(pieces_dict.items(), key=lambda kvp: (kvp[0], kvp[1]["composer"]))
for name, data in sorted_pieces:
    print(f"{name} -> Composer: {data['composer']}, Key: {data['key']}")
