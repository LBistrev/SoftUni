string = input().split()
list_of_string = []
for i in string:
    num = int(i)
    if num > 0:
        list_of_string.append(num * -1)
    else:
        list_of_string.append(abs(num))

print(list_of_string)
