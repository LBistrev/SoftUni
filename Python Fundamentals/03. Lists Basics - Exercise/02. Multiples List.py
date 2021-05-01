factor = int(input())
count = int(input())

result = factor * count

list_lin = []
for num in range(factor, result + 1):
    if num % factor == 0:
        list_lin.append(num)

print(list_lin)
