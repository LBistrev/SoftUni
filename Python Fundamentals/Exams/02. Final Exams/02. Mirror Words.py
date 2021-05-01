import re
words = input()
pattern = r"(@|#)(?P<first_word>[A-Za-z]{3,})\1\1(?P<second_word>[A-Za-z]{3,})\1"
valid_words = [word.groupdict() for word in re.finditer(pattern, words)]
valid = {}
if valid_words:
    print(f"{len(valid_words)} word pairs found!")
    for el in valid_words:
        second = el["second_word"]
        reversed_second = second[::-1]
        if el["first_word"] == reversed_second:
            valid[el["first_word"]] = second
    if valid:
        valid_pairs = []
        print("The mirror words are:")
        for first, second in valid.items():
            valid_pairs.append(f"{first} <=> {second}")
        print(", ".join(valid_pairs))
    else:
        print("No mirror words!")
else:
    print("No word pairs found!")
    print("No mirror words!")
