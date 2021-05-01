message = input().split()

for word in message:
    num = ""
    for ch in word:
        if ch.isdigit():
            num += ch
    char_as_num = chr(int(num))
    end_word = char_as_num + word[len(num):]
    end_word = list(end_word)
    end_word[1], end_word[-1] = end_word[-1], end_word[1]
    print(f"{''.join(end_word)} ", end="")
