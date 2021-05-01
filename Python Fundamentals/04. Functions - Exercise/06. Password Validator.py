def if_the_password_is_valid(code):
    is_valid = True
    count_digit = 0
    if len(code) < 6 or len(code) > 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")
    for pword in code:
        if not pword.isdigit() and not pword.isalpha():
            is_valid = False
            print("Password must consist only of letters and digits")
            break
        if pword.isdigit():
            count_digit += 1
    if count_digit < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    return is_valid


password = input()
if if_the_password_is_valid(password):
    print("Password is valid")
