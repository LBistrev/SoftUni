def string_with_all_characters_between(strin1, string2):
    for char in range(ord(strin1) + 1, ord(string2)):
        print(chr(char), end=" ")


text_1 = input()
text_2 = input()
string_with_all_characters_between(text_1, text_2)
