numbers = int(input())
num = 1
electrons = []

while numbers > 0:
    max_el = 2 * num ** 2
    if max_el > numbers:
        electrons.append(numbers)
    else:
        electrons.append(max_el)
    numbers -= max_el
    num += 1

print(electrons)
