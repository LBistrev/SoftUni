parentheses = input()

stack = []
is_valid = True
for symbol in parentheses:
    if symbol in "{[(":
        stack.append(symbol)
    elif symbol in ")]}":
        if len(stack) == 0:
            is_valid = False
            break
        open_symbol = stack.pop()
        if f"{open_symbol}{symbol}" not in ["()", "[]", "{}"]:
            is_valid = False
            break
            # if symbol == "(" and open_symbol == ")":
            #     continue
            # elif symbol == "[" and open_symbol == "]":
            #     continue
            # elif symbol == "{" and open_symbol == "}":
            #     continue

if is_valid and len(stack) == 0:
    print("YES")
else:
    print("NO")



