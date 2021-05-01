text_1 = input()
text_2 = input()

n = len(text_1)
result = ""
previous_str = text_1
for index in range(len(text_1)):
    for i in range(index+1):
        result += text_2[i]

    for i in range(index+1, len(text_2)):
        result += text_1[i]
    if not result == previous_str:
        print(result)
    previous_str = result
    result = ""

# first = input()
# second = input()
# for i in range(len(first)):
#     if first[i] != second[i]:
#         first = first[: i] + second[i] + first[i+1 :]
#         print(first)
