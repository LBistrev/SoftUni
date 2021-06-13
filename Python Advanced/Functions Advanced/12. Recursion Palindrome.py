def palindrome(word, index=0):

    if index >= len(word) - 1 - index:
        return f"{word} is a palindrome"

    left_letter = word[index]
    right_most_letter = word[- 1 - index]

    if left_letter != right_most_letter:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)
