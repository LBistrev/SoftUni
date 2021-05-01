def is_a_palindrome(list_of_str):
    is_valid = True
    lis = []
    for string in list_of_str:
        num = string[::-1]
        if string == num:
            is_valid = True
            lis.append(is_valid)
        else:
            is_valid = False
            lis.append(is_valid)
    return lis


list_of_strings = input().split(", ")
result = is_a_palindrome(list_of_strings)
for res in result:
    print(res)
