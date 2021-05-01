number = int(input())

total_sum = 0

for letter in range(number):
    letters = input()
    total_sum += (ord(letters))

print(f"The sum equals: {total_sum}")
